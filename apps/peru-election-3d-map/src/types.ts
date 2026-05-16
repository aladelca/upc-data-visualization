import type { Feature, FeatureCollection, MultiPolygon, Point, Polygon } from "geojson";

export type Winner = "peru_libre" | "fuerza_popular" | "EMPATE" | "missing";

export type HeightMetric = "margin" | "validVotes" | "marginVotes";

export type LayerMode = "columns" | "extruded";

export type MapTheme = "light" | "dark";

export type DistrictProperties = {
  ubigeo: string;
  geo_ubigeo: string;
  department: string;
  province: string;
  district: string;
  winner: Winner;
  winner_party: string;
  votes_peru_libre: number;
  votes_fuerza_popular: number;
  blank_votes: number;
  null_votes: number;
  challenged_votes: number;
  citizens_voted: number;
  eligible_voters: number;
  polling_tables: number;
  valid_votes: number;
  total_votes: number;
  peru_libre_pct: number;
  fuerza_popular_pct: number;
  margin_votes: number;
  margin_pct: number;
  turnout_pct: number;
  height_margin: number;
  height_log_valid_votes: number;
  height_log_margin_votes: number;
  join_status: "matched" | "matched_by_name" | "missing_results";
};

export type DistrictPointFeature = Feature<Point, DistrictProperties>;
export type DistrictPolygonFeature = Feature<Polygon | MultiPolygon, DistrictProperties>;

export type DistrictPointCollection = FeatureCollection<Point, DistrictProperties>;
export type DistrictPolygonCollection = FeatureCollection<Polygon | MultiPolygon, DistrictProperties>;

export type ElectionData = {
  centroids: DistrictPointCollection;
  districts: DistrictPolygonCollection;
  isSample: boolean;
};

export type VisualizationState = {
  layerMode: LayerMode;
  heightMetric: HeightMetric;
  theme: MapTheme;
  verticalScale: number;
};
