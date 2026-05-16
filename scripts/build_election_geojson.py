from __future__ import annotations

import argparse
import copy
import json
import shutil
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast

import pandas as pd

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.election_geo_processing import (
    FUERZA_POPULAR,
    PERU_LIBRE,
    TIE,
    aggregate_votes_by_district,
    approximate_centroid,
    feature_ubigeo,
    validate_geo_join,
)
from scripts.http_utils import read_url_bytes

DEPARTMENT_NAMES = {
    "01": "AMAZONAS",
    "02": "ANCASH",
    "03": "APURIMAC",
    "04": "AREQUIPA",
    "05": "AYACUCHO",
    "06": "CAJAMARCA",
    "07": "CALLAO",
    "08": "CUSCO",
    "09": "HUANCAVELICA",
    "10": "HUANUCO",
    "11": "ICA",
    "12": "JUNIN",
    "13": "LA LIBERTAD",
    "14": "LAMBAYEQUE",
    "15": "LIMA",
    "16": "LORETO",
    "17": "MADRE DE DIOS",
    "18": "MOQUEGUA",
    "19": "PASCO",
    "20": "PIURA",
    "21": "PUNO",
    "22": "SAN MARTIN",
    "23": "TACNA",
    "24": "TUMBES",
    "25": "UCAYALI",
}

DEFAULT_DISTRICTS_WFS_URL = (
    "https://geoespacial.inei.gob.pe/geoserver/Interoperabilidad/ows?"
    "service=WFS&version=1.0.0&request=GetFeature&"
    "typeName=Interoperabilidad%3Aig_distrito&maxFeatures=5000&"
    "outputFormat=application%2Fjson"
)

OUTPUT_POLYGONS = "peru_districts_election_2021.geojson"
OUTPUT_CENTROIDS = "peru_district_centroids_election_2021.geojson"
OUTPUT_REPORT = "peru_districts_election_2021_join_report.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build district-level GeoJSON files for the Peru 2021 runoff map."
    )
    parser.add_argument("--onpe", required=True, type=Path)
    parser.add_argument("--districts", default=DEFAULT_DISTRICTS_WFS_URL)
    parser.add_argument("--out", default="data/processed", type=Path)
    parser.add_argument("--public-out", type=Path)
    parser.add_argument(
        "--counted-status",
        action="append",
        default=None,
        help=(
            "Acta status to include. Pass multiple times. "
            "Defaults to CONTABILIZADA and COMPUTADA RESUELTA."
        ),
    )
    parser.add_argument("--skip-polygons", action="store_true")
    return parser.parse_args()


def read_onpe_table(path: Path) -> pd.DataFrame:
    compression = "zip" if path.suffix.lower() == ".zip" else None
    for encoding in ("utf-8", "latin-1"):
        try:
            return pd.read_csv(
                path,
                sep=";",
                dtype={"UBIGEO": "string"},
                compression=compression,
                keep_default_na=False,
                encoding=encoding,
                index_col=False,
            )
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError("utf-8", b"", 0, 1, f"Unable to decode {path}")


def read_geojson(source: str) -> dict[str, Any]:
    if source.startswith(("http://", "https://")):
        return cast(dict[str, Any], json.loads(read_url_bytes(source).decode("utf-8")))

    with Path(source).open(encoding="utf-8") as file:
        return cast(dict[str, Any], json.load(file))


def json_ready(value: Any) -> Any:
    if value is pd.NA or pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def empty_result_properties(ubigeo: str, geo_properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "ubigeo": ubigeo,
        "geo_ubigeo": ubigeo,
        "department": "",
        "province": "",
        "district": str(geo_properties.get("nombdist", "")),
        "winner": "missing",
        "winner_party": "Sin resultado ONPE unido",
        "votes_peru_libre": 0,
        "votes_fuerza_popular": 0,
        "blank_votes": 0,
        "null_votes": 0,
        "challenged_votes": 0,
        "citizens_voted": 0,
        "eligible_voters": 0,
        "polling_tables": 0,
        "valid_votes": 0,
        "total_votes": 0,
        "peru_libre_pct": 0.0,
        "fuerza_popular_pct": 0.0,
        "margin_votes": 0,
        "margin_pct": 0.0,
        "turnout_pct": 0.0,
        "height_margin": 0,
        "height_log_valid_votes": 0,
        "height_log_margin_votes": 0,
        "join_status": "missing_results",
    }


def result_properties(
    geo_ubigeo: str,
    row: dict[str, Any] | None,
    geo_properties: dict[str, Any],
    *,
    join_status: str,
) -> dict[str, Any]:
    if row is None:
        return empty_result_properties(geo_ubigeo, geo_properties)

    properties = {
        "ubigeo": row["ubigeo"],
        "geo_ubigeo": geo_ubigeo,
        "department": row["department"],
        "province": row["province"],
        "district": row["district"],
        "winner": row["winner"],
        "winner_party": row["winner_party"],
        "votes_peru_libre": row["votes_peru_libre"],
        "votes_fuerza_popular": row["votes_fuerza_popular"],
        "blank_votes": row["blank_votes"],
        "null_votes": row["null_votes"],
        "challenged_votes": row["challenged_votes"],
        "citizens_voted": row["citizens_voted"],
        "eligible_voters": row["eligible_voters"],
        "polling_tables": row["polling_tables"],
        "valid_votes": row["valid_votes"],
        "total_votes": row["total_votes"],
        "peru_libre_pct": row["peru_libre_pct"],
        "fuerza_popular_pct": row["fuerza_popular_pct"],
        "margin_votes": row["margin_votes"],
        "margin_pct": row["margin_pct"],
        "turnout_pct": row["turnout_pct"],
        "height_margin": row["height_margin"],
        "height_log_valid_votes": row["height_log_valid_votes"],
        "height_log_margin_votes": row["height_log_margin_votes"],
        "join_status": join_status,
    }
    return {key: json_ready(value) for key, value in properties.items()}


def normalized_name(value: object) -> str:
    text = str(value).strip().upper()
    return " ".join(text.split())


def unique_department_district_index(
    results: pd.DataFrame,
) -> dict[tuple[str, str], dict[str, Any]]:
    records = results.to_dict(orient="records")
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        key = (normalized_name(record["department"]), normalized_name(record["district"]))
        buckets.setdefault(key, []).append(record)

    return {key: rows[0] for key, rows in buckets.items() if len(rows) == 1}


def geo_department_name(properties: dict[str, Any]) -> str:
    code = str(properties.get("ccdd", "")).zfill(2)
    return DEPARTMENT_NAMES.get(code, "")


def build_geojson(
    districts_geojson: dict[str, Any],
    results: pd.DataFrame,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    result_records = results.to_dict(orient="records")
    result_by_ubigeo = {str(record["ubigeo"]): record for record in result_records}
    result_by_name = unique_department_district_index(results)
    geo_ubigeos: list[str] = []
    polygon_features: list[dict[str, Any]] = []
    centroid_features: list[dict[str, Any]] = []
    matched_result_ubigeos: set[str] = set()
    matched_by_ubigeo = 0
    matched_by_name = 0

    for original_feature in districts_geojson.get("features", []):
        feature = copy.deepcopy(original_feature)
        geo_properties = dict(feature.get("properties", {}))
        ubigeo = feature_ubigeo(geo_properties)
        geo_ubigeos.append(ubigeo)
        row = result_by_ubigeo.get(ubigeo)
        join_status = "matched"
        if row is None:
            key = (
                normalized_name(geo_department_name(geo_properties)),
                normalized_name(geo_properties.get("nombdist", "")),
            )
            row = result_by_name.get(key)
            join_status = "matched_by_name" if row is not None else "missing_results"

        if row is not None:
            matched_result_ubigeos.add(str(row["ubigeo"]))
            if join_status == "matched_by_name":
                matched_by_name += 1
            else:
                matched_by_ubigeo += 1

        properties = result_properties(
            ubigeo,
            row,
            geo_properties,
            join_status=join_status,
        )

        feature["properties"] = properties
        polygon_features.append(feature)

        lng, lat = approximate_centroid(feature["geometry"])
        centroid_features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [lng, lat]},
                "properties": properties,
            }
        )

    report: dict[str, Any] = dict(validate_geo_join(results["ubigeo"], geo_ubigeos))
    report["matched_features"] = matched_by_ubigeo + matched_by_name
    report["matched_by_ubigeo"] = matched_by_ubigeo
    report["matched_by_name"] = matched_by_name
    report["unmatched_geo_features"] = len(geo_ubigeos) - report["matched_features"]
    report["unmatched_result_rows_after_name_fallback"] = len(set(results["ubigeo"])) - len(
        matched_result_ubigeos
    )
    return (
        {"type": "FeatureCollection", "features": polygon_features},
        {"type": "FeatureCollection", "features": centroid_features},
        report,
    )


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def copy_to_public(out: Path, public_out: Path) -> None:
    public_out.mkdir(parents=True, exist_ok=True)
    for name in (OUTPUT_POLYGONS, OUTPUT_CENTROIDS, OUTPUT_REPORT):
        source = out / name
        if source.exists():
            shutil.copy2(source, public_out / name)


def main() -> None:
    args = parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    onpe = read_onpe_table(args.onpe)
    counted_status = args.counted_status or ["CONTABILIZADA", "COMPUTADA RESUELTA"]
    results = aggregate_votes_by_district(onpe, counted_status=counted_status)
    districts = read_geojson(str(args.districts))
    polygons, centroids, report = build_geojson(districts, results)

    if not args.skip_polygons:
        write_json(args.out / OUTPUT_POLYGONS, polygons)
    write_json(args.out / OUTPUT_CENTROIDS, centroids)
    write_json(args.out / OUTPUT_REPORT, report)

    if args.public_out is not None:
        copy_to_public(args.out, args.public_out)

    print(
        "Built election GeoJSON: "
        f"{report['matched_features']}/{report['geo_rows']} geo features matched "
        f"({report['matched_by_ubigeo']} by ubigeo, {report['matched_by_name']} by name). "
        f"{report['unmatched_geo_features']} geo features remain unmatched."
    )
    print(f"Parties: {PERU_LIBRE} / {FUERZA_POPULAR}; tie label: {TIE}")


if __name__ == "__main__":
    main()
