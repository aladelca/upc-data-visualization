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

function statusMessage(districtCount: number, isSample: boolean): string {
  return isSample
    ? "Muestra de demostracion. Ejecuta el pipeline para cargar todos los distritos."
    : `${districtCount} distritos cargados desde datos procesados.`;
}

async function loadCentroids(): Promise<{data: DistrictPointCollection; isSample: boolean}> {
  return loadCollection<DistrictPointCollection>(
    DATA_URLS.centroids.primary,
    DATA_URLS.centroids.sample,
  );
}

async function loadDistricts(): Promise<{data: DistrictPolygonCollection; isSample: boolean}> {
  return loadCollection<DistrictPolygonCollection>(
    DATA_URLS.districts.primary,
    DATA_URLS.districts.sample,
  );
}

async function main(): Promise<void> {
  const mapContainer = document.getElementById("map");
  if (!(mapContainer instanceof HTMLElement)) {
    throw new Error("Missing map container");
  }

  const controls = readControls();
  const centroids = await loadCentroids();
  let isSample = centroids.isSample;
  const data: ElectionData = {
    centroids: centroids.data,
    isSample,
  };
  const map = new ElectionMap(mapContainer, data, initialState);
  let loadingDistricts: Promise<boolean> | null = null;
  let latestState = initialState;

  const ensureDistricts = (): Promise<boolean> => {
    if (map.hasDistricts()) {
      return Promise.resolve(true);
    }
    if (loadingDistricts !== null) {
      return loadingDistricts;
    }

    setStatus(controls.status, "Cargando poligonos distritales...");
    loadingDistricts = loadDistricts()
      .then((districts) => {
        isSample = isSample || districts.isSample;
        map.setDistricts(districts.data, districts.isSample);
        setStatus(
          controls.status,
          statusMessage(centroids.data.features.length, isSample),
          isSample,
        );
        return true;
      })
      .catch((error: unknown) => {
        const message =
          error instanceof Error ? error.message : "No se pudieron cargar los poligonos distritales";
        setStatus(controls.status, message, true);
        return false;
      })
      .finally(() => {
        loadingDistricts = null;
      });
    return loadingDistricts;
  };

  const handleStateChange = async (state: VisualizationState): Promise<void> => {
    latestState = state;
    if (state.layerMode === "extruded") {
      const loaded = await ensureDistricts();
      if (!loaded || latestState !== state) {
        map.update(latestState);
        return;
      }
    }
    map.update(state);
  };

  bindControls(controls, initialState, {
    onChange: (state) => {
      void handleStateChange(state);
    },
    onFit: () => map.fitToPeru(),
  });

  setStatus(controls.status, statusMessage(centroids.data.features.length, isSample), isSample);
}

main().catch((error: unknown) => {
  const controls = readControls();
  const message = error instanceof Error ? error.message : "Error desconocido";
  setStatus(controls.status, message, true);
  console.error(error);
});
