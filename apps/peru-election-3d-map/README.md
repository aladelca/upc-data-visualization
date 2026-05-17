# Mapa electoral 3D Peru 2021

App web para visualizar resultados distritales de la segunda vuelta presidencial 2021 con `deck.gl` y `MapLibre GL JS`.

## Ejecutar la app

```bash
npm install --prefix apps/peru-election-3d-map
npm run dev --prefix apps/peru-election-3d-map
```

La app abre en `http://localhost:5174`. Si los GeoJSON completos no existen, carga una muestra de demostracion incluida en `public/data/`.

## Generar datos completos

Desde la raiz del repositorio:

```bash
python3 scripts/download_election_sources.py --include-districts --include-population
python3 scripts/build_election_geojson.py \
  --onpe data/raw/onpe_segunda_vuelta_2021.zip \
  --districts data/raw/inei_distritos_2023.geojson \
  --population data/raw/inei_poblacion_distrital_2017.geojson \
  --out data/processed \
  --public-out apps/peru-election-3d-map/public/data
```

El pipeline produce:

- `peru_district_centroids_election_2021.geojson`: puntos distritales para `ColumnLayer`.
- `peru_districts_election_2021.geojson`: poligonos distritales para extrusiones.
- `peru_districts_election_2021_join_report.json`: reporte de ubigeos faltantes o duplicados.

El color codifica el porcentaje obtenido por el candidato ganador: rojo continuo para Peru Libre y naranja continuo para Fuerza Popular. La altura codifica poblacion total distrital en escala logaritmica usando la capa INEI `ig_pobtotal_dist`.

## Validacion

```bash
npm run typecheck --prefix apps/peru-election-3d-map
npm run lint --prefix apps/peru-election-3d-map
npm run build --prefix apps/peru-election-3d-map
```
