import pandas as pd
import pytest

from scripts.election_geo_processing import (
    FUERZA_POPULAR,
    PERU_LIBRE,
    aggregate_votes_by_district,
    approximate_centroid,
    normalize_ubigeo,
    validate_geo_join,
)


def test_normalize_ubigeo_pads_left_zeroes_and_rejects_invalid_values() -> None:
    assert normalize_ubigeo(10101) == "010101"
    assert normalize_ubigeo("010101") == "010101"
    assert normalize_ubigeo("10101.0") == "010101"

    with pytest.raises(ValueError):
        normalize_ubigeo("not-a-code")


def test_aggregate_votes_by_district_calculates_winner_margin_and_turnout() -> None:
    df = pd.DataFrame(
        {
            "UBIGEO": [10101, "010101", "020101"],
            "DEPARTAMENTO": ["AMAZONAS", "AMAZONAS", "ANCASH"],
            "PROVINCIA": ["CHACHAPOYAS", "CHACHAPOYAS", "HUARAZ"],
            "DISTRITO": ["CHACHAPOYAS", "CHACHAPOYAS", "HUARAZ"],
            "DESCRIP_ESTADO_ACTA": ["CONTABILIZADA", "CONTABILIZADA", "CONTABILIZADA"],
            "VOTOS_P1": [100, 80, 30],
            "VOTOS_P2": [60, 70, 90],
            "VOTOS_VB": [1, None, 2],
            "VOTOS_VN": [4, 2, 3],
            "VOTOS_VI": [0, 0, None],
            "N_CVAS": [165, 152, 125],
            "N_ELEC_HABIL": [300, 250, 200],
        }
    )

    result = aggregate_votes_by_district(df)

    chachapoyas = result[result["ubigeo"] == "010101"].iloc[0]
    assert chachapoyas["votes_peru_libre"] == 180
    assert chachapoyas["votes_fuerza_popular"] == 130
    assert chachapoyas["winner"] == "peru_libre"
    assert chachapoyas["winner_party"] == PERU_LIBRE
    assert chachapoyas["valid_votes"] == 310
    assert chachapoyas["margin_votes"] == 50
    assert chachapoyas["peru_libre_pct"] == pytest.approx(180 / 310)
    assert chachapoyas["turnout_pct"] == pytest.approx(317 / 550)

    huaraz = result[result["ubigeo"] == "020101"].iloc[0]
    assert huaraz["winner_party"] == FUERZA_POPULAR


def test_aggregate_votes_by_district_filters_non_counted_actas_by_default() -> None:
    df = pd.DataFrame(
        {
            "UBIGEO": [10101, 10101],
            "DEPARTAMENTO": ["AMAZONAS", "AMAZONAS"],
            "PROVINCIA": ["CHACHAPOYAS", "CHACHAPOYAS"],
            "DISTRITO": ["CHACHAPOYAS", "CHACHAPOYAS"],
            "DESCRIP_ESTADO_ACTA": ["CONTABILIZADA", "ANULADA"],
            "VOTOS_P1": [100, 999],
            "VOTOS_P2": [60, 999],
        }
    )

    result = aggregate_votes_by_district(df)

    assert result.iloc[0]["votes_peru_libre"] == 100
    assert result.iloc[0]["votes_fuerza_popular"] == 60


def test_validate_geo_join_reports_missing_and_duplicate_ubigeos() -> None:
    report = validate_geo_join(
        result_ubigeos=["010101", "020101", "030101"],
        geo_ubigeos=["010101", "020101", "020101", "040101"],
    )

    assert report["duplicate_geo_ubigeos"] == ["020101"]
    assert report["missing_in_geo"] == ["030101"]
    assert report["missing_results"] == ["040101"]


def test_approximate_centroid_uses_geometry_bounds() -> None:
    geometry = {
        "type": "Polygon",
        "coordinates": [[[-80.0, -12.0], [-78.0, -12.0], [-78.0, -10.0], [-80.0, -10.0]]],
    }

    assert approximate_centroid(geometry) == (-79.0, -11.0)
