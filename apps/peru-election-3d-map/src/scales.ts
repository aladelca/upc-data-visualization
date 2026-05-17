import type { DistrictProperties, HeightMetric } from "./types";

export type Rgba = [number, number, number, number];

const PERU_LIBRE_LIGHT: Rgba = [250, 214, 210, 230];
const PERU_LIBRE_STRONG: Rgba = [172, 28, 42, 235];
const FUERZA_POPULAR_LIGHT: Rgba = [252, 225, 190, 230];
const FUERZA_POPULAR_STRONG: Rgba = [221, 113, 32, 235];
const NEUTRAL: Rgba = [148, 156, 168, 190];

function interpolateColor(start: Rgba, end: Rgba, ratio: number, alpha?: number): Rgba {
  const safeRatio = Math.max(0, Math.min(1, ratio));
  return [
    Math.round(start[0] + (end[0] - start[0]) * safeRatio),
    Math.round(start[1] + (end[1] - start[1]) * safeRatio),
    Math.round(start[2] + (end[2] - start[2]) * safeRatio),
    alpha ?? Math.round(start[3] + (end[3] - start[3]) * safeRatio),
  ];
}

function winnerShare(properties: DistrictProperties): number {
  if (properties.winner === "peru_libre") {
    return properties.peru_libre_pct;
  }
  if (properties.winner === "fuerza_popular") {
    return properties.fuerza_popular_pct;
  }
  return 0;
}

export function voteShareColor(properties: DistrictProperties, alpha?: number): Rgba {
  if (properties.join_status === "missing_results" || properties.winner === "missing") {
    return alpha === undefined ? NEUTRAL : [NEUTRAL[0], NEUTRAL[1], NEUTRAL[2], alpha];
  }
  if (properties.winner === "EMPATE") {
    return alpha === undefined ? NEUTRAL : [NEUTRAL[0], NEUTRAL[1], NEUTRAL[2], alpha];
  }

  const share = winnerShare(properties);
  const intensity = Math.max(0, Math.min(1, (share - 0.5) / 0.5));
  if (properties.winner === "peru_libre") {
    return interpolateColor(PERU_LIBRE_LIGHT, PERU_LIBRE_STRONG, intensity, alpha);
  }
  return interpolateColor(FUERZA_POPULAR_LIGHT, FUERZA_POPULAR_STRONG, intensity, alpha);
}

export function heightValue(properties: DistrictProperties, metric: HeightMetric): number {
  if (properties.population_join_status === "missing_population") {
    return 0;
  }

  switch (metric) {
    case "population":
      return properties.height_log_population;
  }
}

export const integerFormatter = new Intl.NumberFormat("es-PE", {
  maximumFractionDigits: 0,
});

export const percentFormatter = new Intl.NumberFormat("es-PE", {
  maximumFractionDigits: 1,
  minimumFractionDigits: 1,
  style: "percent",
});
