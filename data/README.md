# Datos para el mapa electoral 3D

Esta carpeta separa fuentes originales (`raw/`) de artefactos generados (`processed/`).

## Fuentes

- ONPE: `Resultados por mesa de las Elecciones Presidenciales 2021 Segunda Vuelta`.
  - Dataset: `https://www.datosabiertos.gob.pe/dataset/resultados-por-mesa-de-las-elecciones-presidenciales-2021-segunda-vuelta-oficina-nacional-de`
  - Recurso completo: `https://cuentadatosabiertos.blob.core.windows.net/dataset/Resultados_2da_vuelta_Version_ONPE.zip`
  - Diccionario: `https://www.datosabiertos.gob.pe/sites/default/files/Diccionario_EleccionesPresidenciales_2021_2daVuelta_ONPE.xlsx`
- INEI IDE: capa distrital `Interoperabilidad:ig_distrito`.
  - WFS: `https://geoespacial.inei.gob.pe/geoserver/Interoperabilidad/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Interoperabilidad%3Aig_distrito&maxFeatures=5000&outputFormat=application%2Fjson`
  - Descarga alternativa: `https://ide.inei.gob.pe/files/Distrito.rar`
- INEI IDE: poblacion total distrital `Interoperabilidad:ig_pobtotal_dist`.
  - WFS: `https://geoespacial.inei.gob.pe/geoserver/Interoperabilidad/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Interoperabilidad%3Aig_pobtotal_dist&maxFeatures=5000&outputFormat=application%2Fjson`
  - Fuente declarada por la capa: `INEI - CPV2017 RESULTADOS`.

## Convenciones

- `VOTOS_P1` corresponde a `PARTIDO POLITICO NACIONAL PERU LIBRE`.
- `VOTOS_P2` corresponde a `FUERZA POPULAR`.
- El join territorial usa `UBIGEO` normalizado a seis digitos.
- La geometria distrital disponible en IDE INEI esta actualizada al 2023; si se usa para 2021, las diferencias por cambios distritales deben quedar documentadas en el reporte de join.

## Flujo recomendado

```bash
python3 scripts/download_election_sources.py --include-districts --include-population
python3 scripts/build_election_geojson.py \
  --onpe data/raw/onpe_segunda_vuelta_2021.zip \
  --districts data/raw/inei_distritos_2023.geojson \
  --population data/raw/inei_poblacion_distrital_2017.geojson \
  --out data/processed \
  --public-out apps/peru-election-3d-map/public/data
```

Los archivos reales generados quedan ignorados por git. La app incluye una muestra pequena solo para poder abrir la interfaz antes de ejecutar el pipeline completo.
