from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.http_utils import read_url_bytes

ONPE_ZIP_URL = (
    "https://cuentadatosabiertos.blob.core.windows.net/dataset/"
    "Resultados_2da_vuelta_Version_ONPE.zip"
)
ONPE_SAMPLE_URL = (
    "https://www.datosabiertos.gob.pe/sites/default/files/Muestra_2da_vuelta_Version_ONPE_0.csv"
)
ONPE_DICTIONARY_URL = (
    "https://www.datosabiertos.gob.pe/sites/default/files/"
    "Diccionario_EleccionesPresidenciales_2021_2daVuelta_ONPE.xlsx"
)
INEI_DISTRICTS_WFS_URL = (
    "https://geoespacial.inei.gob.pe/geoserver/Interoperabilidad/ows?"
    "service=WFS&version=1.0.0&request=GetFeature&"
    "typeName=Interoperabilidad%3Aig_distrito&maxFeatures=5000&"
    "outputFormat=application%2Fjson"
)
INEI_POPULATION_WFS_URL = (
    "https://geoespacial.inei.gob.pe/geoserver/Interoperabilidad/ows?"
    "service=WFS&version=1.0.0&request=GetFeature&"
    "typeName=Interoperabilidad%3Aig_pobtotal_dist&maxFeatures=5000&"
    "outputFormat=application%2Fjson"
)


def download(url: str, target: Path, *, overwrite: bool) -> None:
    if target.exists() and not overwrite:
        return

    target.write_bytes(read_url_bytes(url))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download ONPE and INEI source files for the Peru 2021 election map."
    )
    parser.add_argument("--out", default="data/raw", type=Path)
    parser.add_argument("--include-districts", action="store_true")
    parser.add_argument("--include-population", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    resources: list[tuple[str, Path]] = [
        (ONPE_ZIP_URL, args.out / "onpe_segunda_vuelta_2021.zip"),
        (ONPE_SAMPLE_URL, args.out / "onpe_segunda_vuelta_2021_sample.csv"),
        (ONPE_DICTIONARY_URL, args.out / "onpe_segunda_vuelta_2021_dictionary.xlsx"),
    ]
    if args.include_districts:
        resources.append((INEI_DISTRICTS_WFS_URL, args.out / "inei_distritos_2023.geojson"))
    if args.include_population:
        resources.append(
            (INEI_POPULATION_WFS_URL, args.out / "inei_poblacion_distrital_2017.geojson")
        )

    manifest_resources: list[dict[str, str | int]] = []
    manifest = {
        "downloaded_at": datetime.now(UTC).isoformat(),
        "resources": manifest_resources,
    }
    for url, target in resources:
        download(url, target, overwrite=args.overwrite)
        manifest_resources.append(
            {
                "url": url,
                "path": str(target),
                "bytes": target.stat().st_size,
            }
        )

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
