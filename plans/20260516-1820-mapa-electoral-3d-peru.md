# Mapa electoral 3D de Peru 2021 por distrito

## Goal

- Construir una app web interactiva, fuera de notebooks, que replique el lenguaje visual del mapa 3D de densidad poblacional de Mapas Milhaud usando resultados distritales de la segunda vuelta presidencial de Peru 2021.
- El producto debe mostrar una columna por distrito como vista principal, con color por porcentaje obtenido por el candidato ganador y altura por poblacion distrital, e incluir una vista alternativa con distritos extruidos.
- El pipeline de datos debe ser reproducible: descargar o registrar fuentes, agregar resultados ONPE por distrito, unir con geometria distrital INEI, unir poblacion distrital INEI, calcular metricas y exportar GeoJSON optimizado para la app.

## Request Snapshot

- User request: "quiero hacer uno igual pero con los resultados por distrito de la segunda vuelta de las elecciones presidenciales en peru 2021; si no tuviera que ser un notebook, que me sugieres? haz un plan para esto"
- Owner or issue: `None`
- Plan file: `plans/20260516-1820-mapa-electoral-3d-peru.md`

## Current State

- El repositorio esta orientado a curso de `Data Visualization` con notebooks en `notebooks/` y guias del trabajo final centradas en `Tableau` y Python.
- No existe configuracion de app web: no hay `package.json`, `vite.config.*`, `tsconfig.json` ni estructura `src/`.
- No existe configuracion Python declarativa: no hay `pyproject.toml`, `requirements.txt`, `setup.cfg`, `tox.ini` ni `pytest.ini`, aunque si existen caches de Ruff, mypy y pytest.
- Hay tests Python actuales en `tests/test_preprocessing.py`, con `tests/conftest.py` agregando la raiz al `sys.path`.
- Archivos inspeccionados:
  - `notebooks/README.md`
  - `notebooks/semana-11-comparacion-transversal-mapas.ipynb`
  - `notebooks/semana-13-dashboard-engineering.ipynb`
  - `tests/test_preprocessing.py`
  - `tests/conftest.py`
  - `trabajo-final-guia-para-estudiantes.md`
  - `propuesta-trabajo-final-con-entregas-parciales.md`
  - `scripts/`

## Findings

- El grafico de referencia es un mapa 3D de columnas, no un coropletico plano. La pagina indica que se construye generando columnas cuya altura representa densidad poblacional.
- La fuente oficial electoral relevante es el dataset de Datos Abiertos "Resultados por mesa de las Elecciones Presidenciales 2021 Segunda Vuelta - ONPE", publicado el 2021-06-18 y modificado el 2021-06-30.
- La geometria distrital puede obtenerse desde el geoportal IDE INEI mediante capas WMS/WFS distritales, o descargarse como capa cartografica y versionarse como fuente raw si el endpoint no es estable.
- Para emular el estilo visual, `deck.gl` es mejor que Tableau o matplotlib porque soporta `ColumnLayer`, `GeoJsonLayer` extruido, iluminacion, tooltips y controles interactivos en navegador.
- Para mantener rigor de datos, el frontend no debe agregar votos ni poblacion. La agregacion por ubigeo y los joins territoriales deben quedar resueltos antes de publicar el GeoJSON.
- La altura del mapa usa poblacion total distrital de la capa INEI `Interoperabilidad:ig_pobtotal_dist`, cuya fuente declarada es `INEI - CPV2017 RESULTADOS`.

## Scope

### In scope

- Crear una app web independiente en `apps/peru-election-3d-map/` usando Vite, TypeScript, `deck.gl` y `MapLibre GL JS`.
- Crear un pipeline Python en `scripts/` para preparar datos electorales y geograficos.
- Definir archivos de datos raw y processed con convenciones claras.
- Agregar tests Python para agregacion electoral, calculo de ganador, margen, normalizacion de alturas, join por ubigeo y join de poblacion.
- Agregar configuracion minima de Ruff, mypy y pytest en `pyproject.toml`.
- Agregar scripts npm para `dev`, `build`, `typecheck` y `lint` de la app.
- Incluir documentacion corta de ejecucion y fuentes.

### Out of scope

- Publicar en Vercel u otro hosting.
- Reemplazar el trabajo final en Tableau del curso.
- Hacer un analisis politico interpretativo extenso.
- Usar datos no oficiales o scraping si la descarga oficial funciona.
- Resolver cambios historicos de limites distritales posteriores a 2021 mas alla de documentar el criterio de geometria usado.

## File Plan

| Path | Action | Details |
| --- | --- | --- |
| `pyproject.toml` | create | Definir dependencias Python, configuracion de Ruff, mypy y pytest para el pipeline. Incluir `pandas`, `geopandas`, `pyogrio`, `shapely`, `requests`, `mapclassify` y tipos necesarios si aplican. |
| `data/raw/.gitkeep` | create | Mantener carpeta para fuentes originales descargadas o colocadas manualmente. |
| `data/processed/.gitkeep` | create | Mantener carpeta para artefactos reproducibles generados. |
| `data/README.md` | create | Documentar fuentes ONPE e INEI, licencia, fecha de descarga, granularidad y criterios de join por ubigeo. |
| `scripts/download_election_sources.py` | create | Descargar la data ONPE y, si el servicio lo permite, la geometria distrital y poblacion distrital INEI. Si no, validar presencia de archivos manuales en `data/raw/`. |
| `scripts/build_election_geojson.py` | create | Leer resultados por mesa, agregar por distrito, calcular metricas electorales, unir con geometria y poblacion, generar centroides y exportar GeoJSON procesado. |
| `scripts/election_geo_processing.py` | create | Concentrar funciones testeables: normalizar ubigeo, agregar votos, calcular ganador, calcular alturas, validar cardinalidad del join y simplificar columnas. |
| `tests/test_election_geo_processing.py` | create | Cubrir casos base y borde del pipeline con data sintetica. |
| `apps/peru-election-3d-map/package.json` | create | Definir dependencias frontend y scripts npm. |
| `apps/peru-election-3d-map/index.html` | create | Entry HTML de la app Vite. |
| `apps/peru-election-3d-map/tsconfig.json` | create | Configuracion TypeScript estricta para la app. |
| `apps/peru-election-3d-map/vite.config.ts` | create | Configuracion Vite y ruta publica de datos. |
| `apps/peru-election-3d-map/src/main.ts` | create | Montar la app, cargar datos y conectar controles con capas. |
| `apps/peru-election-3d-map/src/map.ts` | create | Construir `Deck`, `MapView`, `ColumnLayer`, `GeoJsonLayer`, tooltips, iluminacion y transiciones. |
| `apps/peru-election-3d-map/src/scales.ts` | create | Escalas de color por porcentaje del ganador y altura por poblacion. |
| `apps/peru-election-3d-map/src/types.ts` | create | Tipos TypeScript del GeoJSON procesado y estado de visualizacion. |
| `apps/peru-election-3d-map/src/ui.ts` | create | Controles de capa, escala vertical, tema y leyenda. |
| `apps/peru-election-3d-map/src/styles.css` | create | Estilos de layout, paneles, leyenda, tooltip y estados responsive. |
| `apps/peru-election-3d-map/public/data/.gitkeep` | create | Destino para copiar el GeoJSON optimizado que consumira la app. |
| `apps/peru-election-3d-map/README.md` | create | Instrucciones de instalacion, procesamiento de datos, ejecucion local y build. |

## Data and Contract Changes

- Input ONPE:
  - Fuente: Datos Abiertos Peru, dataset ONPE de segunda vuelta presidencial 2021 por mesa.
  - Granularidad: mesa de sufragio.
  - Campos esperados: ubigeo o campos territoriales equivalentes, organizacion politica, votos, votos blancos/nulos si vienen en la fuente, electores habilitados o emitidos si estan disponibles.
- Input INEI:
  - Fuente: IDE INEI, capa distrital WFS o descarga de capa cartografica.
  - Granularidad: distrito.
  - Campo clave esperado: `ubigeo` de 6 digitos o equivalente normalizable.
- Input INEI poblacion:
  - Fuente: IDE INEI, capa WFS `Interoperabilidad:ig_pobtotal_dist`.
  - Granularidad: distrito.
  - Campo clave esperado: `ubigeo`; campo de medida: `pobtotal`.
  - Fuente declarada por la capa: `INEI - CPV2017 RESULTADOS`.
- Output principal:
  - `data/processed/peru_districts_election_2021.geojson`
  - `apps/peru-election-3d-map/public/data/peru_districts_election_2021.geojson`
- Output auxiliar:
  - `data/processed/peru_district_centroids_election_2021.geojson`
  - `apps/peru-election-3d-map/public/data/peru_district_centroids_election_2021.geojson`
- Propiedades GeoJSON minimas:
  - `ubigeo`
  - `department`
  - `province`
  - `district`
  - `winner`
  - `winner_party`
  - `votes_peru_libre`
  - `votes_fuerza_popular`
  - `valid_votes`
  - `total_votes`
  - `peru_libre_pct`
  - `fuerza_popular_pct`
  - `margin_votes`
  - `margin_pct`
  - `height_margin`
  - `height_log_valid_votes`
  - `population_total`
  - `height_log_population`
  - `population_join_status`
  - `join_status`
- Frontend contract:
  - La app debe tratar el GeoJSON procesado como solo lectura.
  - La app puede cambiar visualmente la escala vertical, pero no recalcular resultados electorales ni poblacion base.

## Implementation Steps

1. Crear `pyproject.toml` con configuracion de herramientas y dependencias Python necesarias para el pipeline geoespacial.
2. Crear estructura `data/raw/`, `data/processed/` y `data/README.md` con convenciones de fuentes, descargas y artefactos generados.
3. Implementar `scripts/election_geo_processing.py` con funciones puras:
   - `normalize_ubigeo`
   - `aggregate_votes_by_district`
   - `calculate_district_result`
   - `calculate_height_metrics`
   - `validate_geo_join`
4. Implementar `scripts/download_election_sources.py` para descargar ONPE desde Datos Abiertos y registrar metadatos locales. Para INEI, descargar geometria distrital y poblacion por endpoint WFS cuando este disponible; si falla o requiere flujo manual, dejar error claro con instrucciones.
5. Implementar `scripts/build_election_geojson.py` como comando reproducible:
   - leer raw ONPE
   - leer geometria distrital
   - normalizar ubigeos
   - agregar resultados por distrito
   - validar que no haya duplicidad de ubigeo en geometria
   - calcular ganador y margen
   - unir poblacion total distrital por `ubigeo`, con fallback por nombre unico de departamento + distrito
   - calcular centroides aproximados para la capa de columnas
   - simplificar geometria para web sin romper topologia de forma visible
   - exportar GeoJSON procesados
6. Crear tests en `tests/test_election_geo_processing.py` con data sintetica para:
   - ubigeos con ceros iniciales
   - empate tecnico o votos faltantes
   - distritos con una sola mesa
   - distritos con mesas de ambos partidos
   - join incompleto entre resultados y geometria
   - altura poblacional en escala logaritmica para evitar que Lima aplaste la escala visual
7. Crear app Vite en `apps/peru-election-3d-map/` con TypeScript estricto.
8. Implementar carga de GeoJSON desde `public/data/`.
9. Implementar `ColumnLayer` como vista principal:
   - posicion: centroide distrital
   - radio: escala fija con ajuste por zoom si hace falta
   - color: porcentaje del candidato ganador, con escala continua por partido
   - elevacion: `height_log_population`
10. Implementar `GeoJsonLayer` extruido como vista alternativa:
    - color: porcentaje del candidato ganador, con escala continua por partido
    - elevacion: `height_log_population`
    - bordes sutiles para legibilidad
11. Implementar UI:
    - selector de capa: columnas / distritos extruidos
    - selector de altura: poblacion total
    - toggle de mapa base claro/oscuro si no complica rendimiento
    - leyenda de colores
    - tooltip con distrito, provincia, departamento, ganador, porcentajes y margen
12. Ajustar diseno responsive:
    - mapa full viewport
    - panel lateral compacto en desktop
    - panel inferior colapsable en mobile
13. Optimizar datos:
    - medir tamano del GeoJSON
    - si es pesado, simplificar con `mapshaper` o exportar TopoJSON como segunda iteracion
14. Documentar ejecucion en `apps/peru-election-3d-map/README.md`.
15. Correr validaciones Python y frontend desde la raiz y corregir hallazgos.

## Tests

- Unit: `tests/test_election_geo_processing.py` cubrir agregacion por distrito, normalizacion de ubigeo, ganador, margen, alturas y poblacion.
- Integration: `tests/test_election_geo_processing.py` validar un join sintetico resultados-geometria con filas faltantes y duplicadas.
- Regression: mantener `tests/test_preprocessing.py` sin cambios funcionales; correrlo para asegurar que la nueva configuracion no rompe tests existentes.
- Frontend type/regression: `npm run typecheck --prefix apps/peru-election-3d-map` y `npm run build --prefix apps/peru-election-3d-map`.
- Optional visual QA: abrir la app local y verificar en navegador que el canvas no este en blanco, que los tooltips funcionen y que el panel no tape informacion critica en mobile.

## Validation

- Format: `python -m ruff format --check scripts tests`
- Lint: `python -m ruff check scripts tests`
- Types: `python -m mypy scripts tests`
- Tests: `python -m pytest tests`
- Frontend install: `npm install --prefix apps/peru-election-3d-map`
- Frontend types: `npm run typecheck --prefix apps/peru-election-3d-map`
- Frontend lint: `npm run lint --prefix apps/peru-election-3d-map`
- Frontend build: `npm run build --prefix apps/peru-election-3d-map`
- Data download: `python scripts/download_election_sources.py --include-districts --include-population`
- Data build: `python scripts/build_election_geojson.py --onpe data/raw/onpe_segunda_vuelta_2021.zip --districts data/raw/inei_distritos_2023.geojson --population data/raw/inei_poblacion_distrital_2017.geojson --out data/processed --public-out apps/peru-election-3d-map/public/data`

## Risks and Mitigations

- Riesgo: la geometria distrital actual no coincide exactamente con distritos existentes en 2021. -> Mitigar documentando fecha/fuente de geometria, revisando ubigeos no empatados y creando reporte de join.
- Riesgo: el dataset ONPE por mesa no trae un ubigeo limpio o usa nombres territoriales. -> Mitigar normalizando con diccionario ONPE/INEI y fallando si hay ambiguedades.
- Riesgo: el GeoJSON distrital completo puede ser pesado para navegador. -> Mitigar simplificando geometria, exportando centroides para `ColumnLayer` y reservando poligonos para una vista alternativa.
- Riesgo: altura por poblacion produce dominancia visual de Lima. -> Mitigar usando escala logaritmica y control de escala vertical.
- Riesgo: la poblacion disponible es CPV2017 y no una estimacion exacta para 2021. -> Mitigar documentando la fuente declarada por la capa y manteniendo `population_join_status` en el GeoJSON.
- Riesgo: colores politicos pueden tener contraste insuficiente o sesgo visual. -> Mitigar con paleta divergente sobria, leyenda explicita y prueba de contraste.
- Riesgo: `MapLibre` requiere tiles externos. -> Mitigar usando un estilo publico estable o permitiendo fallback sin mapa base, con contorno de Peru y fondo neutro.

## Open Questions

- None

## Acceptance Criteria

- La app muestra un mapa 3D nacional con una columna por distrito y tooltips informativos.
- El color identifica correctamente el partido ganador y la intensidad representa el porcentaje obtenido por ese candidato.
- La altura representa poblacion total distrital en escala logaritmica para evitar que Lima domine el grafico.
- Existe una vista alternativa de distritos extruidos.
- El pipeline genera GeoJSON procesado desde fuentes raw sin edicion manual de resultados.
- El join entre resultados y geometria produce un reporte de distritos no empatados o confirma cero faltantes.
- La app corre localmente con `npm run dev --prefix apps/peru-election-3d-map`.
- El build de frontend termina correctamente.
- `ruff`, `mypy` y `pytest` pasan para los archivos Python involucrados.

## Definition of Done

- Codigo Python del pipeline implementado y testeado.
- App web TypeScript implementada con `deck.gl` y `MapLibre GL JS`.
- Datos procesados reproducibles o instrucciones claras para generarlos desde `data/raw/`.
- Documentacion de fuentes, comandos y limitaciones actualizada.
- Validaciones Python y frontend en verde.
- Plan actualizado si cambia el alcance, la fuente de datos o la estrategia de visualizacion.

## Implementation Notes

- Implementacion creada en `apps/peru-election-3d-map/` con Vite, TypeScript, `deck.gl` y `MapLibre GL JS`.
- El pipeline quedo en `scripts/download_election_sources.py`, `scripts/build_election_geojson.py`, `scripts/election_geo_processing.py` y `scripts/http_utils.py`.
- Se evito depender obligatoriamente de `geopandas` para reducir friccion de instalacion; el join y los centroides aproximados se hacen sobre GeoJSON.
- Al probar ONPE + WFS INEI, el join directo por `ubigeo` solo empato `1102` de `1890` geometrias. Se agrego fallback conservador por `departamento + distrito` cuando el nombre es unico dentro del departamento. Con eso el build real empato `1845` de `1890` geometrias: `1102` por ubigeo y `743` por nombre.
- Se agrego descarga y join de poblacion distrital desde `Interoperabilidad:ig_pobtotal_dist`; el build real empato `1874` de `1890` geometrias por `ubigeo`.
- La visualizacion final codifica color con una escala continua por porcentaje del candidato ganador y altura con `height_log_population`.
- Los GeoJSON completos generados pesan aproximadamente `1.4 MB` para centroides y `46 MB` para poligonos, por lo que quedan ignorados por git. La app incluye muestras pequenas para abrir sin ejecutar el pipeline.
- Validaciones ejecutadas:
  - `.venv/bin/python -m ruff format --check scripts/__init__.py scripts/http_utils.py scripts/election_geo_processing.py scripts/download_election_sources.py scripts/build_election_geojson.py tests/test_election_geo_processing.py`
  - `.venv/bin/python -m ruff check scripts/__init__.py scripts/http_utils.py scripts/election_geo_processing.py scripts/download_election_sources.py scripts/build_election_geojson.py tests/test_election_geo_processing.py`
  - `.venv/bin/python -m mypy scripts/__init__.py scripts/http_utils.py scripts/election_geo_processing.py scripts/download_election_sources.py scripts/build_election_geojson.py tests/test_election_geo_processing.py`
  - `.venv/bin/python -m pytest tests/test_election_geo_processing.py tests/test_preprocessing.py`
  - `npm run typecheck --prefix apps/peru-election-3d-map`
  - `npm run lint --prefix apps/peru-election-3d-map`
  - `npm run build --prefix apps/peru-election-3d-map`
