import type { DistrictProperties, HeightMetric, Winner } from "./types";

export type Rgba = [number, number, number, number];

const PARTY_COLORS: Record<Winner, Rgba> = {
  peru_libre: [190, 38, 45, 230],
  fuerza_popular: [232, 132, 45, 230],
  EMPATE: [125, 132, 143, 210],
  missing: [125, 132, 143, 170],
};

export function winnerColor(winner: Winner, alpha?: number): Rgba {
  const color = PARTY_COLORS[winner] ?? PARTY_COLORS.missing;
  return alpha === undefined ? color : [color[0], color[1], color[2], alpha];
}

export function heightValue(properties: DistrictProperties, metric: HeightMetric): number {
  if (properties.join_status !== "matched") {
    return 0;
  }

  switch (metric) {
    case "validVotes":
      return properties.height_log_valid_votes;
    case "marginVotes":
      return properties.height_log_margin_votes;
    case "margin":
      return properties.height_margin;
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
