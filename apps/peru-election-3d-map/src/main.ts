import "./styles.css";

import { ElectionMap } from "./map";
import { bindControls, readControls, setStatus } from "./ui";
import type {
  DistrictPointCollection,
  DistrictPolygonCollection,
  ElectionData,
  VisualizationState,
} from "./types";

const initialState: VisualizationState = {
  layerMode: "columns",
  heightMetric: "population",
  theme: "light",
  verticalScale: 1,
};

const DATA_URLS = {
  centroids: {
    primary: "/data/peru_district_centroids_election_2021.geojson",
    sample: "/data/sample_district_centroids_election_2021.geojson",
  },
  districts: {
    primary: "/data/peru_districts_election_2021.geojson",
    sample: "/data/sample_districts_election_2021.geojson",
  },
};

async function loadCollection<T>(primary: string, sample: string): Promise<{data: T; isSample: boolean}> {
  const primaryResponse = await fetch(primary);
  if (primaryResponse.ok) {
    return {data: (await primaryResponse.json()) as T, isSample: false};
  }

  const sampleResponse = await fetch(sample);
  if (!sampleResponse.ok) {
    throw new Error(`No se pudo cargar ${primary} ni ${sample}`);
  }
  return {data: (await sampleResponse.json()) as T, isSample: true};
}

async function loadElectionData(): Promise<ElectionData> {
  const [centroids, districts] = await Promise.all([
    loadCollection<DistrictPointCollection>(DATA_URLS.centroids.primary, DATA_URLS.centroids.sample),
    loadCollection<DistrictPolygonCollection>(DATA_URLS.districts.primary, DATA_URLS.districts.sample),
  ]);

  return {
    centroids: centroids.data,
    districts: districts.data,
    isSample: centroids.isSample || districts.isSample,
  };
}

async function main(): Promise<void> {
  const mapContainer = document.getElementById("map");
  if (!(mapContainer instanceof HTMLElement)) {
    throw new Error("Missing map container");
  }

  const controls = readControls();
  const data = await loadElectionData();
  const map = new ElectionMap(mapContainer, data, initialState);

  bindControls(controls, initialState, {
    onChange: (state) => map.update(state),
    onFit: () => map.fitToPeru(),
  });

  setStatus(
    controls.status,
    data.isSample
      ? "Muestra de demostracion. Ejecuta el pipeline para cargar todos los distritos."
      : `${data.centroids.features.length} distritos cargados desde datos procesados.`,
    data.isSample,
  );
}

main().catch((error: unknown) => {
  const controls = readControls();
  const message = error instanceof Error ? error.message : "Error desconocido";
  setStatus(controls.status, message, true);
  console.error(error);
});
