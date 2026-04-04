# Plan de Contenido de 14 Semanas

Basado en el sílabo del curso `1ACC0211 - Data Visualization`.

## Criterio de ajuste

- El sílabo original indica 16 semanas.
- Para este plan se consideran 14 semanas de desarrollo de contenido.
- Se asume una sesión semanal de 4 horas.
- Carga total de clase: 56 horas.
- Se toma como base la sumilla y las unidades temáticas del sílabo:
  - Introducción a la visualización de datos
  - Análisis exploratorio de datos
  - Gobierno de datos
  - Agregación y reducción de datos
  - Visualización exploratoria
  - Interpretación de resultados
  - Visualización explicativa
  - Tipos de visualizaciones
  - Presentaciones de alto impacto
  - Accesibilidad y estética
  - Visualización longitudinal
  - Visualización transversal
  - Formatos para idiomas gráficos

## Estructura sugerida para cada sesión de 4 horas

- 60 min: conceptos y discusión guiada.
- 90 min: demostración, análisis de casos o taller práctico.
- 60 min: trabajo aplicado con datos.
- 30 min: cierre, retroalimentación y encargo.

## Opción 1: Plan Base Balanceado

| Semana | Horas | Tema central | Contenidos específicos | Actividad sugerida | Entregable sugerido |
|---|---:|---|---|---|---|
| 1 | 4 | Introducción al curso y valor de la visualización | Rol de la visualización en la toma de decisiones, ejemplos efectivos y deficientes, tipos de usuarios y contextos de consumo de información | Discusión de casos y diagnóstico inicial de visualizaciones reales | Ficha de análisis de 2 visualizaciones |
| 2 | 4 | Análisis exploratorio de datos I | Tipos de variables, estadística descriptiva, preguntas analíticas, lectura inicial de un dataset | Exploración guiada de un conjunto de datos | Resumen exploratorio inicial |
| 3 | 4 | Gobierno y calidad de datos | Calidad de datos, consistencia, valores faltantes, sesgos, trazabilidad, diccionario de datos | Auditoría simple de calidad de datos | Documento corto de hallazgos de calidad |
| 4 | 4 | Agregación, reducción y transformación | Granularidad, agrupaciones, filtros, tablas resumen, variables derivadas, reducción para comunicar | Taller de transformación de datos | Dataset preparado para visualizar |
| 5 | 4 | Visualización exploratoria I | Gráficos para comparación y distribución: barras, histogramas, boxplots, densidades | Construcción y crítica comparativa de gráficos | Set de 4 visualizaciones exploratorias |
| 6 | 4 | Visualización exploratoria II e interpretación | Relación entre variables, correlación, segmentación, outliers, patrones, lectura crítica de resultados | Taller de interpretación y explicación de hallazgos | Informe breve de insights exploratorios |
| 7 | 4 | Visualización explicativa | Diferencia entre explorar y explicar, foco narrativo, títulos efectivos, anotaciones, jerarquía del mensaje | Rediseño de un gráfico exploratorio en pieza explicativa | Una visualización explicativa comentada |
| 8 | 4 | Tipos de visualización y criterio de selección | Cuándo usar barras, líneas, dispersión, heatmaps, mapas, treemaps, tablas; errores frecuentes de selección | Matriz de decisión de gráficos según objetivo analítico | Guía propia de selección de gráficos |
| 9 | 4 | Accesibilidad y percepción visual | Color, contraste, paletas seguras, legibilidad, tipografía, principios perceptivos, diseño inclusivo | Revisión de accesibilidad de piezas existentes | Checklist aplicado a una visualización |
| 10 | 4 | Estética y presentaciones de alto impacto | Composición, alineación, espacio en blanco, resaltado visual, ritmo narrativo, diseño para exposición | Taller de mejora visual de una presentación | 3 diapositivas de alto impacto |
| 11 | 4 | Visualización longitudinal | Series de tiempo, tendencias, variación, estacionalidad, ventanas de comparación, errores comunes en ejes temporales | Análisis de un caso temporal | Dashboard o lámina temporal |
| 12 | 4 | Visualización transversal | Comparación entre grupos, categorías, cohortes, regiones o segmentos; lectura de diferencias y composición | Caso aplicado con comparación multigrupo | Set de gráficos comparativos |
| 13 | 4 | Formatos para idiomas gráficos | Dashboard, reporte ejecutivo, infografía y presentación; ventajas, limitaciones y criterios de uso | Evaluación de formato según audiencia | Propuesta de formato final con boceto |
| 14 | 4 | Integración y data storytelling | Construcción de narrativa, secuencia de insights, recomendaciones y cierre ejecutivo | Presentación final o revisión cruzada entre equipos | Producto integrador final |

## Opción 2: Plan Técnico Recomendado con Foco en Tableau

Esta variante mantiene los temas del sílabo, pero los lleva a un terreno más técnico y aplicado. El eje principal es `Tableau`, con una revisión comparativa de `Power BI` en momentos puntuales. También incorpora preparación y limpieza de datos, modelado básico de fuentes, expresiones calculadas, dashboards interactivos y una introducción a técnicas avanzadas de visualización para datos de alta dimensionalidad como `t-SNE`.

### Herramientas sugeridas

- Herramienta principal: `Tableau Desktop` o `Tableau Public`.
- Herramienta secundaria: `Power BI` para comparación de flujos y capacidades.
- Soporte para preparación de datos: `Excel`, `CSV`, `SQL` básico o `Python` con `pandas`.
- Opcional para técnicas avanzadas: `Python` con `scikit-learn` para `PCA` y `t-SNE`, exportando luego los resultados a Tableau.

### Enfoque técnico por sesión de 4 horas

- 45 min: fundamentos conceptuales y decisión de diseño.
- 60 min: demostración técnica en Tableau.
- 105 min: laboratorio guiado con datos reales.
- 30 min: revisión de resultados y cierre.

### Cronograma técnico sugerido

| Semana | Horas | Enfoque técnico | Contenidos clave | Producto o laboratorio |
|---|---:|---|---|---|
| 1 | 4 | Introducción técnica al curso y ecosistema de herramientas | Rol de la visualización en analítica, diferencia entre Tableau y Power BI, instalación, conexión a fuentes, interfaz de Tableau, hojas, dashboards e historias | Dataset elegido y primer workbook conectado |
| 2 | 4 | Perfilado y comprensión del dato | Tipos de datos, dimensiones y medidas, niveles de granularidad, calidad del dato, detección de nulos, duplicados, inconsistencias y sesgos | Perfil exploratorio del dataset y checklist de calidad |
| 3 | 4 | Limpieza y preparación de datos I | Renombrado de campos, cambio de tipos, manejo de nulos, filtros de limpieza, split, pivot, unpivot, estandarización de categorías | Dataset limpio y documentado para visualización |
| 4 | 4 | Preparación de datos II y modelado de fuente | Joins, unions, relationships, blending, agregación, tablas analíticas, campos calculados básicos, jerarquías | Fuente de datos modelada y lista para análisis |
| 5 | 4 | Visualización exploratoria básica en Tableau | Barras, líneas, dispersión, histogramas, boxplots, tablas de resumen, buenas prácticas de lectura inicial | Workbook con visualizaciones exploratorias base |
| 6 | 4 | Visualización analítica e interpretación | Segmentación, filtros, grupos, sets, bins, highlight, outliers, correlación visual, comparación entre variables | Dashboard exploratorio con hallazgos preliminares |
| 7 | 4 | Cálculos y analítica intermedia | Campos calculados, parámetros, reference lines, trend lines, table calculations, percent of total, running total | Tablero analítico con métricas derivadas |
| 8 | 4 | Visualización explicativa y storytelling técnico | Selección de gráficos según objetivo, títulos analíticos, anotaciones, tooltips útiles, storytelling en Tableau | Historia visual explicativa con 3 a 5 vistas |
| 9 | 4 | Diseño, accesibilidad y usabilidad | Paletas seguras, contraste, tipografía, etiquetado, layout, containers, device design, jerarquía visual | Rediseño accesible de un dashboard previo |
| 10 | 4 | Visualización longitudinal | Series temporales, jerarquías de fecha, tendencias, estacionalidad, moving averages, comparación temporal y forecasting básico | Dashboard temporal orientado a análisis de evolución |
| 11 | 4 | Visualización transversal y comparativa | Comparación entre segmentos, categorías y regiones, mapas, heatmaps, highlight tables, treemaps y small multiples | Vista comparativa para toma de decisiones |
| 12 | 4 | Técnicas avanzadas de visualización | Introducción a reducción de dimensionalidad, `PCA` y `t-SNE`, cuándo usarlos, limitaciones, cómo generar embeddings fuera de Tableau y visualizarlos dentro de Tableau | Visualización de alta dimensionalidad usando proyección previa |
| 13 | 4 | Ingeniería de dashboards y publicación | Actions, filter actions, highlight actions, navegación entre vistas, performance básica, publicación en Tableau Public, contraste rápido con Power BI | Dashboard final navegable y publicable |
| 14 | 4 | Proyecto integrador técnico | Integración de preparación, análisis, diseño y narrativa; defensa técnica del workflow y del producto visual | Entrega final en Tableau con presentación breve |

### Notas metodológicas para esta opción

- `Tableau` debe ser la herramienta principal del curso para mantener coherencia en entregables y curva de aprendizaje.
- `Power BI` puede aparecer en una sesión comparativa breve o como referencia para estudiantes que ya lo usen, pero no conviene dividir el curso en dos herramientas principales.
- `t-SNE` no debe enseñarse como un gráfico más, sino como una técnica avanzada de proyección para explorar datos de alta dimensionalidad.
- Para `t-SNE`, lo más realista es calcular la proyección en `Python` o en otra herramienta externa y luego llevar el resultado a Tableau para su interpretación visual.
- Si el grupo tiene menos base técnica, `PCA` puede introducirse primero y `t-SNE` dejarse como extensión opcional o laboratorio guiado.

## Opción 3: Plan con Mayor Enfoque Ejecutivo y Comunicación

Esta variante es útil si el curso apunta a perfiles que necesitan comunicar hallazgos a usuarios no técnicos.

| Semana | Horas | Enfoque | Actividad principal |
|---|---:|---|---|
| 1 | 4 | El valor de visualizar para decidir | Discusión de casos empresariales |
| 2 | 4 | Entender los datos antes de comunicarlos | Lectura guiada de dataset y preguntas clave |
| 3 | 4 | Calidad, contexto y confianza en los datos | Evaluación de riesgos de interpretación |
| 4 | 4 | Simplificación y síntesis del dato | Taller de reducción de complejidad |
| 5 | 4 | Gráficos que ayudan a descubrir | Exploración visual con foco en hallazgos |
| 6 | 4 | Cómo interpretar resultados correctamente | Redacción de insights con evidencia |
| 7 | 4 | Cómo construir una historia con datos | Transformar análisis en mensaje |
| 8 | 4 | Elegir el gráfico adecuado para convencer | Comparación crítica de alternativas |
| 9 | 4 | Accesibilidad y claridad visual | Ajustes visuales para distintas audiencias |
| 10 | 4 | Presentaciones de alto impacto | Diseño de presentación ejecutiva |
| 11 | 4 | Mostrar cambios en el tiempo | Narrativa temporal para negocio |
| 12 | 4 | Comparar segmentos y perfiles | Storytelling comparativo |
| 13 | 4 | Elegir el formato correcto | Dashboard vs reporte vs presentación |
| 14 | 4 | Presentación integradora final | Exposición final con retroalimentación |

## Contenido adicional recomendado

Si se quiere enriquecer el sílabo, conviene agregar estos temas sin salir del enfoque del curso:

- Ética y honestidad visual: escalas truncadas, cherry-picking, dobles ejes y sesgos de presentación.
- Storytelling con datos: estructura narrativa, contexto, tensión, hallazgo y recomendación.
- Diseño de dashboards: KPI, jerarquía visual, filtros, navegación y consistencia.
- Preparación técnica del dato: joins, unions, relationships, blending y control de granularidad.
- Cálculos analíticos en Tableau: table calculations, campos calculados, parámetros y métricas derivadas.
- Rendimiento y publicación: optimización básica de dashboards y despliegue en Tableau Public.
- Crítica de visualizaciones reales: análisis de dashboards públicos, medios y reportes empresariales.
- Buenas prácticas de color y percepción: principios de preatención, contraste y agrupación visual.
- Comunicación para distintas audiencias: técnico, ejecutivo, cliente y público general.

## Sugerencia de entregables durante el ciclo

- Semana 3: análisis de una mala y una buena visualización.
- Semana 5: paquete de visualizaciones exploratorias.
- Semana 7: visualización explicativa individual.
- Semana 10: presentación breve de alto impacto.
- Semana 13: propuesta de dashboard o reporte final.
- Semana 14: entrega integradora final.

## Recomendación final

La opción más sólida para este curso, si quieres un perfil más aplicado y empleable, es la **Opción 2**, porque permite trabajar el ciclo completo: preparación del dato, análisis, diseño visual, interactividad y publicación.

El mejor enfoque es usar `Tableau` como herramienta central y dejar `Power BI` como referencia secundaria o comparativa.

Si el objetivo principal fuera comunicación ejecutiva por encima del trabajo técnico, entonces convendría la **Opción 3**.
