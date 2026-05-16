import { MapboxOverlay } from "@deck.gl/mapbox";
import type { PickingInfo, Position } from "@deck.gl/core";
import { ColumnLayer, GeoJsonLayer } from "@deck.gl/layers";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

import { heightValue, integerFormatter, percentFormatter, winnerColor } from "./scales";
import type {
  DistrictPointFeature,
  DistrictPolygonFeature,
  DistrictProperties,
  ElectionData,
  VisualizationState,
} from "./types";

const INITIAL_CENTER: [number, number] = [-75.4, -9.4];

const LIGHT_STYLE = "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json";
const DARK_STYLE = "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json";

export class ElectionMap {
  private readonly map: maplibregl.Map;
  private readonly overlay: MapboxOverlay;
  private state: VisualizationState;
  private loaded = false;

  constructor(container: HTMLElement, private readonly data: ElectionData, state: VisualizationState) {
    this.state = state;
    this.map = new maplibregl.Map({
      container,
      style: LIGHT_STYLE,
      center: INITIAL_CENTER,
      zoom: 4.35,
      minZoom: 3.4,
      maxZoom: 12,
      pitch: 54,
      bearing: -18,
      canvasContextAttributes: {antialias: true},
      attributionControl: {compact: true},
    });

    this.overlay = new MapboxOverlay({
      interleaved: false,
      layers: [],
      getTooltip: (info: PickingInfo<DistrictPointFeature | DistrictPolygonFeature>) =>
        tooltip(info.object),
    });

    void this.map.once("load", () => {
      this.loaded = true;
      this.map.addControl(
        new maplibregl.NavigationControl({showCompass: true, showZoom: true, visualizePitch: true}),
        "top-right",
      );
      this.map.addControl(this.overlay);
      this.render();
    });
  }

  update(state: VisualizationState): void {
    const themeChanged = state.theme !== this.state.theme;
    this.state = state;

    if (themeChanged) {
      this.map.setStyle(state.theme === "light" ? LIGHT_STYLE : DARK_STYLE);
    }
    if (this.loaded) {
      this.render();
    }
  }

  fitToPeru(): void {
    this.map.easeTo({
      center: INITIAL_CENTER,
      zoom: 4.35,
      pitch: 54,
      bearing: -18,
      duration: 700,
    });
  }

  private render(): void {
    this.overlay.setProps({
      layers:
        this.state.layerMode === "columns"
          ? [this.columnLayer()]
          : [this.extrudedDistrictLayer()],
    });
  }

  private columnLayer(): ColumnLayer<DistrictPointFeature> {
    return new ColumnLayer<DistrictPointFeature>({
      id: "district-result-columns",
      data: this.data.centroids.features,
      diskResolution: 18,
      radius: 4200,
      extruded: true,
      pickable: true,
      elevationScale: this.state.verticalScale,
      getPosition: (feature) => pointPosition(feature),
      getElevation: (feature) => heightValue(feature.properties, this.state.heightMetric),
      getFillColor: (feature) => winnerColor(feature.properties.winner),
      getLineColor: [22, 24, 29, 130],
      lineWidthMinPixels: 0.5,
      material: {
        ambient: 0.45,
        diffuse: 0.65,
        shininess: 18,
        specularColor: [255, 255, 255],
      },
    });
  }

  private extrudedDistrictLayer(): GeoJsonLayer<DistrictProperties> {
    return new GeoJsonLayer<DistrictProperties>({
      id: "district-result-polygons",
      data: this.data.districts.features,
      extruded: true,
      filled: true,
      stroked: true,
      wireframe: false,
      pickable: true,
      elevationScale: this.state.verticalScale,
      getElevation: (feature) => heightValue(feature.properties, this.state.heightMetric),
      getFillColor: (feature) => winnerColor(feature.properties.winner, 215),
      getLineColor: [246, 248, 250, 160],
      getLineWidth: 1,
      lineWidthUnits: "pixels",
      lineWidthMinPixels: 0.35,
      material: {
        ambient: 0.5,
        diffuse: 0.7,
        shininess: 14,
        specularColor: [255, 255, 255],
      },
    });
  }
}

function pointPosition(feature: DistrictPointFeature): Position {
  const longitude = feature.geometry.coordinates[0] ?? 0;
  const latitude = feature.geometry.coordinates[1] ?? 0;
  return [longitude, latitude];
}

function tooltip(feature: DistrictPointFeature | DistrictPolygonFeature | null | undefined) {
  if (!feature) {
    return null;
  }

  const properties = feature.properties;
  const winner =
    properties.winner === "peru_libre"
      ? "Peru Libre"
      : properties.winner === "fuerza_popular"
        ? "Fuerza Popular"
        : properties.winner_party;

  return {
    html: `
      <div class="tooltip-title">${escapeHtml(properties.district)}</div>
      <div>${escapeHtml(properties.province)} · ${escapeHtml(properties.department)}</div>
      <dl>
        <dt>Ganador</dt><dd>${escapeHtml(winner)}</dd>
        <dt>Peru Libre</dt><dd>${percentFormatter.format(properties.peru_libre_pct)}</dd>
        <dt>Fuerza Popular</dt><dd>${percentFormatter.format(properties.fuerza_popular_pct)}</dd>
        <dt>Margen</dt><dd>${percentFormatter.format(properties.margin_pct)} · ${integerFormatter.format(properties.margin_votes)}</dd>
        <dt>Votos validos</dt><dd>${integerFormatter.format(properties.valid_votes)}</dd>
      </dl>
    `,
  };
}

function escapeHtml(value: string): string {
  return value.replace(
    /[&<>"']/g,
    (character) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      })[character] ?? character,
  );
}
