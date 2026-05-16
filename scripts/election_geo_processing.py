from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, TypedDict

import pandas as pd

PERU_LIBRE = "PARTIDO POLITICO NACIONAL PERU LIBRE"
FUERZA_POPULAR = "FUERZA POPULAR"
TIE = "EMPATE"

PARTY_COLUMNS = {
    "votes_peru_libre": "VOTOS_P1",
    "votes_fuerza_popular": "VOTOS_P2",
}

OPTIONAL_VOTE_COLUMNS = {
    "blank_votes": "VOTOS_VB",
    "null_votes": "VOTOS_VN",
    "challenged_votes": "VOTOS_VI",
}


class JoinReport(TypedDict):
    result_rows: int
    geo_rows: int
    duplicate_geo_ubigeos: list[str]
    missing_in_geo: list[str]
    missing_results: list[str]


def normalize_ubigeo(value: object) -> str:
    """Normalize INEI/ONPE ubigeo values to six digits."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        raise ValueError("ubigeo is missing")

    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]

    digits = re.sub(r"\D", "", text)
    if not digits:
        raise ValueError(f"ubigeo has no digits: {value!r}")
    if len(digits) > 6:
        raise ValueError(f"ubigeo is longer than six digits: {value!r}")
    return digits.zfill(6)


def normalize_ubigeo_series(values: pd.Series) -> pd.Series:
    return values.map(normalize_ubigeo).astype("string")


def _numeric_column(frame: pd.DataFrame, column: str) -> pd.Series:
    if column not in frame.columns:
        return pd.Series(0, index=frame.index, dtype="int64")
    return pd.to_numeric(frame[column], errors="coerce").fillna(0).astype("int64")


def aggregate_votes_by_district(
    frame: pd.DataFrame,
    *,
    status_column: str = "DESCRIP_ESTADO_ACTA",
    counted_status: str | Sequence[str] | None = ("CONTABILIZADA", "COMPUTADA RESUELTA"),
) -> pd.DataFrame:
    working = frame.copy()
    if counted_status is not None and status_column in working.columns:
        statuses = (
            {counted_status.upper()}
            if isinstance(counted_status, str)
            else {status.upper() for status in counted_status}
        )
        working = working[working[status_column].astype("string").str.upper().isin(statuses)]

    if "UBIGEO" not in working.columns:
        raise KeyError("ONPE data must include UBIGEO")

    working["ubigeo"] = normalize_ubigeo_series(working["UBIGEO"])
    working["department"] = working.get("DEPARTAMENTO", "").astype("string").str.strip()
    working["province"] = working.get("PROVINCIA", "").astype("string").str.strip()
    working["district"] = working.get("DISTRITO", "").astype("string").str.strip()

    for output_column, source_column in PARTY_COLUMNS.items():
        working[output_column] = _numeric_column(working, source_column)
    for output_column, source_column in OPTIONAL_VOTE_COLUMNS.items():
        working[output_column] = _numeric_column(working, source_column)

    working["citizens_voted"] = _numeric_column(working, "N_CVAS")
    working["eligible_voters"] = _numeric_column(working, "N_ELEC_HABIL")

    grouped = (
        working.groupby("ubigeo", as_index=False)
        .agg(
            department=("department", "first"),
            province=("province", "first"),
            district=("district", "first"),
            votes_peru_libre=("votes_peru_libre", "sum"),
            votes_fuerza_popular=("votes_fuerza_popular", "sum"),
            blank_votes=("blank_votes", "sum"),
            null_votes=("null_votes", "sum"),
            challenged_votes=("challenged_votes", "sum"),
            citizens_voted=("citizens_voted", "sum"),
            eligible_voters=("eligible_voters", "sum"),
            polling_tables=("ubigeo", "size"),
        )
        .sort_values(["department", "province", "district"], kind="stable")
        .reset_index(drop=True)
    )
    return calculate_district_result(grouped)


def calculate_district_result(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    result["valid_votes"] = result["votes_peru_libre"] + result["votes_fuerza_popular"]
    result["total_votes"] = (
        result["valid_votes"]
        + result["blank_votes"]
        + result["null_votes"]
        + result["challenged_votes"]
    )

    valid = result["valid_votes"].where(result["valid_votes"] > 0)
    result["peru_libre_pct"] = (result["votes_peru_libre"] / valid).fillna(0.0)
    result["fuerza_popular_pct"] = (result["votes_fuerza_popular"] / valid).fillna(0.0)
    result["margin_votes"] = (result["votes_peru_libre"] - result["votes_fuerza_popular"]).abs()
    result["margin_pct"] = (result["margin_votes"] / valid).fillna(0.0)
    result["turnout_pct"] = (
        result["citizens_voted"] / result["eligible_voters"].where(result["eligible_voters"] > 0)
    ).fillna(0.0)

    winner_conditions = [
        result["votes_peru_libre"] > result["votes_fuerza_popular"],
        result["votes_fuerza_popular"] > result["votes_peru_libre"],
    ]
    result["winner"] = TIE
    result.loc[winner_conditions[0], "winner"] = "peru_libre"
    result.loc[winner_conditions[1], "winner"] = "fuerza_popular"
    result["winner_party"] = result["winner"].map(
        {
            "peru_libre": PERU_LIBRE,
            "fuerza_popular": FUERZA_POPULAR,
            TIE: TIE,
        }
    )

    return calculate_height_metrics(result)


def calculate_height_metrics(
    frame: pd.DataFrame,
    *,
    min_height: int = 500,
    margin_height: int = 60000,
    vote_height: int = 80000,
) -> pd.DataFrame:
    result = frame.copy()
    result["height_margin"] = min_height + (result["margin_pct"].clip(0, 1) * margin_height)

    max_valid_votes = max(int(result["valid_votes"].max()), 1)
    result["height_log_valid_votes"] = min_height + (
        result["valid_votes"].map(math.log1p) / math.log1p(max_valid_votes) * vote_height
    )

    max_margin_votes = max(int(result["margin_votes"].max()), 1)
    result["height_log_margin_votes"] = min_height + (
        result["margin_votes"].map(math.log1p) / math.log1p(max_margin_votes) * vote_height
    )

    return result


def validate_geo_join(result_ubigeos: Iterable[str], geo_ubigeos: Iterable[str]) -> JoinReport:
    result_list = [normalize_ubigeo(value) for value in result_ubigeos]
    geo_list = [normalize_ubigeo(value) for value in geo_ubigeos]
    result_set = set(result_list)
    geo_set = set(geo_list)
    duplicate_geo = sorted({ubigeo for ubigeo in geo_list if geo_list.count(ubigeo) > 1})

    return {
        "result_rows": len(result_list),
        "geo_rows": len(geo_list),
        "duplicate_geo_ubigeos": duplicate_geo,
        "missing_in_geo": sorted(result_set - geo_set),
        "missing_results": sorted(geo_set - result_set),
    }


def feature_ubigeo(properties: Mapping[str, Any]) -> str:
    for key in ("ubigeo", "UBIGEO", "codigo", "CODIGO"):
        if key in properties and properties[key] not in (None, ""):
            return normalize_ubigeo(properties[key])

    ccdd = properties.get("ccdd")
    ccpp = properties.get("ccpp")
    ccdi = properties.get("ccdi")
    if ccdd is not None and ccpp is not None and ccdi is not None:
        return normalize_ubigeo(f"{ccdd}{ccpp}{ccdi}")

    raise KeyError("GeoJSON feature does not include a recognizable ubigeo")


def coordinate_bounds(coordinates: Sequence[Any]) -> tuple[float, float, float, float]:
    points: list[tuple[float, float]] = []

    def collect(value: Sequence[Any]) -> None:
        if len(value) >= 2 and all(isinstance(item, int | float) for item in value[:2]):
            points.append((float(value[0]), float(value[1])))
            return
        for item in value:
            if isinstance(item, Sequence):
                collect(item)

    collect(coordinates)
    if not points:
        raise ValueError("geometry has no coordinate points")

    longitudes = [point[0] for point in points]
    latitudes = [point[1] for point in points]
    return min(longitudes), min(latitudes), max(longitudes), max(latitudes)


def approximate_centroid(geometry: Mapping[str, Any]) -> tuple[float, float]:
    bounds = coordinate_bounds(geometry["coordinates"])
    min_lng, min_lat, max_lng, max_lat = bounds
    return ((min_lng + max_lng) / 2, (min_lat + max_lat) / 2)
