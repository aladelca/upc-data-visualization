# Temario Desarrollado de 14 Semanas

Curso orientado a `Data Visualization` con enfoque técnico y aplicado, usando `Tableau` como herramienta principal y `Power BI` como referencia secundaria de contraste.

## Supuestos del diseño

- Duración: 14 semanas.
- Frecuencia: 1 sesión por semana.
- Duración por sesión: 4 horas.
- Carga presencial total: 56 horas.
- Herramienta principal: `Tableau Desktop` o `Tableau Public`.
- Herramientas de soporte: `Excel`, `CSV`, `SQL` básico y `Python` con `pandas` y `scikit-learn` para algunos laboratorios.
- Enfoque: preparación de datos, análisis exploratorio, diseño visual, dashboards interactivos, storytelling técnico y visualización de datos de alta dimensionalidad.

## Estructura sugerida de cada sesión

- Bloque 1, 45 min: fundamentos, marco conceptual y decisiones de diseño.
- Bloque 2, 60 min: demostración técnica guiada.
- Bloque 3, 105 min: laboratorio aplicado con dataset real.
- Bloque 4, 30 min: revisión, discusión de resultados y encargo.

## Resultados generales esperados

Al finalizar el curso, el estudiante será capaz de:

- Perfilar, limpiar y preparar una fuente de datos para análisis visual.
- Diseñar visualizaciones exploratorias y explicativas técnicamente correctas.
- Construir dashboards interactivos en Tableau con criterios de claridad, accesibilidad y rendimiento.
- Justificar la selección de gráficos según la estructura del dato y la pregunta analítica.
- Integrar técnicas avanzadas de visualización, incluyendo proyecciones de dimensionalidad reducida como `PCA` y `t-SNE`, dentro de un flujo de análisis reproducible.

---

## Semana 1: Introducción técnica al curso y ecosistema de visualización

### Objetivo de la semana

Configurar el entorno de trabajo, comprender el rol técnico de la visualización en analítica de datos e identificar la arquitectura básica de trabajo en Tableau.

### Temario desarrollado

- Qué resuelve la visualización de datos dentro de un flujo analítico.
- Diferencia entre análisis exploratorio, análisis explicativo y storytelling.
- Tipos de consumidores de visualización:
  - analista
  - usuario de negocio
  - tomador de decisión
  - público general
- Tipos de productos visuales:
  - hoja de análisis
  - dashboard interactivo
  - historia
  - reporte ejecutivo
- Panorama de herramientas:
  - Tableau
  - Power BI
  - librerías de Python
- Cuándo conviene Tableau frente a Power BI:
  - rapidez para explorar
  - flexibilidad visual
  - prototipado interactivo
  - narrativa visual
- Arquitectura básica de Tableau:
  - conexión a fuente
  - hoja
  - dashboard
  - story
  - data pane
  - shelves y marks card
- Tipos de conexión de datos:
  - archivo plano
  - Excel
  - texto delimitado
  - base de datos
  - extract vs live
- Flujo general del curso:
  - perfilado del dato
  - limpieza
  - modelado básico
  - exploración
  - diseño
  - dashboard final

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - presentación del curso, entregables y stack técnico
  - qué significa "hacer bien" una visualización desde el punto de vista analítico
  - ejemplos de dashboards buenos y deficientes
- Bloque 2:
  - instalación y configuración de Tableau
  - recorrido guiado de la interfaz
  - conexión a un dataset en formato CSV o Excel
- Bloque 3:
  - laboratorio de conexión a una fuente de datos
  - identificación inicial de dimensiones y medidas
  - construcción de una hoja simple con barras y una hoja simple con línea o dispersión
- Bloque 4:
  - revisión de errores comunes en la primera conexión
  - definición del dataset base que se utilizará varias semanas

### Laboratorio sugerido

- Conectar un dataset de ventas, churn, salud, educación o movilidad.
- Crear una hoja con comparación por categoría.
- Crear una hoja con evolución temporal o dispersión entre dos variables.
- Guardar el primer workbook con estructura de carpetas y convención de nombres.

### Producto esperado

- Workbook inicial conectado correctamente.
- Identificación preliminar de campos, tipos y posibles preguntas analíticas.

### Trabajo fuera de clase

- Instalar completamente el entorno si quedó pendiente.
- Explorar el dataset elegido e identificar al menos 5 preguntas analíticas.
- Leer una guía breve sobre diferencias entre `extract` y `live connection`.

---

## Semana 2: Perfilado y comprensión estructural del dato

### Objetivo de la semana

Comprender la estructura técnica del dataset, su granularidad, sus tipos de variables y los principales problemas de calidad que pueden afectar la visualización.

### Temario desarrollado

- Concepto de unidad de análisis.
- Qué es la granularidad y por qué determina el tipo de visualización posible.
- Diferencia entre:
  - registro
  - evento
  - transacción
  - agregado
- Tipos de variables:
  - categóricas nominales
  - categóricas ordinales
  - numéricas discretas
  - numéricas continuas
  - temporales
  - geográficas
- Dimensiones y medidas en Tableau.
- Jerarquías naturales:
  - fecha
  - ubicación
  - producto
  - organización
- Perfilado del dato:
  - conteo de registros
  - cardinalidad por campo
  - porcentaje de nulos
  - frecuencia de categorías
  - rangos mínimos y máximos
  - valores atípicos obvios
- Problemas típicos de calidad:
  - duplicados
  - campos mal tipados
  - categorías inconsistentes
  - fechas inválidas
  - formatos mixtos
  - valores faltantes
- Relación entre calidad de datos y honestidad visual.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - explicación de granularidad, tipos de variables y lectura estructural del dato
  - revisión de preguntas analíticas bien y mal formuladas
- Bloque 2:
  - demostración de perfilado manual y visual en Tableau
  - revisión de campos continuos, discretos y jerarquías automáticas
- Bloque 3:
  - laboratorio de perfilado:
    - conteo de registros
    - exploración de valores únicos
    - revisión de nulos
    - distribución inicial de campos numéricos
    - validación de campos fecha
- Bloque 4:
  - discusión sobre qué preguntas sí y no se pueden responder con la fuente actual
  - definición del checklist de calidad del curso

### Laboratorio sugerido

- Generar una tabla de perfilado del dataset.
- Documentar para cada columna:
  - tipo esperado
  - tipo actual
  - nivel de completitud
  - observaciones
- Detectar al menos 3 riesgos de interpretación por calidad de datos.

### Producto esperado

- Perfil técnico del dataset.
- Checklist de calidad preliminar y registro de problemas detectados.

### Trabajo fuera de clase

- Completar un diccionario de datos simplificado.
- Formular 3 hipótesis de negocio o análisis que luego serán validadas visualmente.

---

## Semana 3: Limpieza y preparación de datos I

### Objetivo de la semana

Aplicar procedimientos de limpieza de datos antes de visualizar, garantizando consistencia semántica y formato adecuado para análisis.

### Temario desarrollado

- Principios de limpieza orientada a visualización.
- Qué limpiar antes de visualizar y qué resolver con transformación posterior.
- Limpieza básica de columnas:
  - renombrado
  - eliminación de espacios
  - normalización de mayúsculas y minúsculas
  - unificación de etiquetas
- Conversión de tipos:
  - texto a fecha
  - texto a número
  - número a categoría
- Tratamiento de valores faltantes:
  - imputación simple
  - exclusión
  - recodificación explícita
  - advertencia metodológica
- Detección de duplicados exactos y funcionales.
- Limpieza de categorías sucias:
  - sinonimia
  - errores de digitación
  - variantes de abreviación
- Operaciones útiles en Tableau y otras herramientas:
  - split
  - custom split
  - pivot
  - unpivot
  - aliases
  - replace references
- Criterios para documentar toda intervención sobre el dato.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - explicación de por qué limpiar modifica el resultado visual
  - revisión de decisiones correctas e incorrectas de limpieza
- Bloque 2:
  - demostración de limpieza en Tableau Data Source y, si hace falta, en Excel o Python
  - manejo de tipos mal inferidos
- Bloque 3:
  - laboratorio guiado de:
    - renombrado de campos
    - corrección de tipos
    - revisión de nulos
    - consolidación de categorías
    - limpieza de fechas
- Bloque 4:
  - discusión sobre qué transformaciones deben quedar documentadas
  - consolidación de una bitácora mínima de preparación

### Laboratorio sugerido

- Limpiar un dataset con errores reales o simulados.
- Crear una tabla "antes vs después" con capturas o métricas:
  - porcentaje de nulos
  - categorías inconsistentes
  - campos corregidos

### Producto esperado

- Dataset limpio y listo para análisis exploratorio.
- Bitácora de limpieza de datos.

### Trabajo fuera de clase

- Formalizar la bitácora.
- Preparar una breve justificación de 3 decisiones de limpieza tomadas.

---

## Semana 4: Preparación de datos II y modelado básico de fuentes

### Objetivo de la semana

Construir una fuente analítica preparada para Tableau usando relaciones entre tablas, agregación controlada y campos calculados iniciales.

### Temario desarrollado

- Conceptos de modelado ligero para visualización.
- Diferencia entre:
  - join
  - union
  - relationship
  - blending
- Cuándo usar cada uno y qué errores produce un mal modelado.
- Riesgos de duplicación por joins de cardinalidad incorrecta.
- Agregación previa vs agregación al vuelo en Tableau.
- Construcción de tablas analíticas.
- Creación de campos calculados básicos:
  - margen
  - tasa
  - porcentaje
  - indicador binario
  - agrupación lógica
- Jerarquías:
  - geográficas
  - temporales
  - organizacionales
- Organización del modelo para rendimiento y legibilidad.
- Validación del modelo:
  - conteos antes y después
  - totales esperados
  - integridad de claves

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de relaciones entre tablas y problemas de cardinalidad
  - ejemplos de duplicación silenciosa en dashboards
- Bloque 2:
  - demostración de joins, relationships y unions en Tableau
  - construcción de campos calculados simples
- Bloque 3:
  - laboratorio de modelado:
    - unir tablas
    - validar conteos
    - crear campos derivados
    - probar jerarquías
- Bloque 4:
  - revisión grupal de fuentes mal modeladas
  - criterios para declarar una fuente "lista para análisis"

### Laboratorio sugerido

- Tomar dos o más tablas relacionadas:
  - ventas y clientes
  - pacientes y visitas
  - productos y transacciones
- Construir una fuente analítica con al menos:
  - una relación o join
  - una jerarquía
  - tres campos calculados

### Producto esperado

- Fuente de datos modelada y validada.
- Registro de cálculos básicos creados.

### Trabajo fuera de clase

- Completar documentación breve del modelo.
- Preparar una explicación de por qué se eligió `join`, `relationship` o `union`.

---

## Semana 5: Visualización exploratoria básica en Tableau

### Objetivo de la semana

Construir visualizaciones exploratorias fundamentales para entender distribución, comparación y evolución inicial de los datos.

### Temario desarrollado

- Qué caracteriza a una visualización exploratoria.
- Principios para explorar sin sobrecargar.
- Gráficos de comparación:
  - barras
  - barras apiladas
  - barras lado a lado
- Gráficos de distribución:
  - histograma
  - boxplot
  - strip plot
- Gráficos de tendencia básica:
  - línea
  - área
- Gráficos de relación:
  - dispersión
  - tamaño por marca
  - color por segmento
- Orden, ranking y top N.
- Uso correcto de etiquetas y tooltips en una fase exploratoria.
- Qué no hacer:
  - 3D
  - demasiadas categorías
  - color sin semántica
  - ejes confusos

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de selección básica de gráficos según pregunta
  - revisión de errores de codificación visual
- Bloque 2:
  - construcción guiada de barras, histogramas, dispersión y línea en Tableau
  - formateo mínimo para legibilidad
- Bloque 3:
  - laboratorio:
    - comparar categorías
    - explorar distribución de una métrica
    - observar tendencia temporal
    - detectar relaciones entre dos variables
- Bloque 4:
  - crítica cruzada entre visualizaciones generadas
  - selección de las vistas base que pasarán al dashboard exploratorio

### Laboratorio sugerido

- Crear al menos 5 hojas exploratorias:
  - una comparación categórica
  - una distribución
  - una serie temporal
  - una dispersión
  - una vista de ranking

### Producto esperado

- Workbook exploratorio base.
- Primer conjunto consistente de hojas con naming y estructura clara.

### Trabajo fuera de clase

- Refinar títulos y tooltips.
- Elegir las 3 mejores vistas y justificar por qué aportan valor analítico.

---

## Semana 6: Visualización analítica, segmentación e interpretación

### Objetivo de la semana

Profundizar el análisis visual mediante filtros, grupos, sets, bins y estrategias de segmentación para obtener hallazgos más específicos.

### Temario desarrollado

- Diferencia entre explorar y analizar con intención.
- Segmentación del dato:
  - por categoría
  - por región
  - por periodo
  - por cohortes simples
- Creación y uso de:
  - filtros
  - quick filters
  - context filters
  - bins
  - groups
  - sets
- Lectura de outliers y anomalías.
- Comparaciones condicionales.
- Correlación visual:
  - qué sugiere
  - qué no demuestra
- Highlighting y drill-down.
- Cómo redactar un insight basado en evidencia visual.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - conceptos de segmentación y análisis condicional
  - discusión sobre correlación vs causalidad
- Bloque 2:
  - demostración de bins, groups, sets y filtros de contexto
  - ejemplos de análisis por segmentos
- Bloque 3:
  - laboratorio:
    - crear segmentos
    - identificar outliers
    - comparar subgrupos
    - preparar un dashboard exploratorio inicial
- Bloque 4:
  - socialización de hallazgos
  - revisión de calidad del insight redactado

### Laboratorio sugerido

- Construir un dashboard exploratorio con:
  - 3 a 4 vistas
  - filtros interactivos
  - al menos un set o bin
  - un hallazgo explícito documentado

### Producto esperado

- Dashboard exploratorio funcional.
- Lista de insights preliminares sustentados visualmente.

### Trabajo fuera de clase

- Redactar entre 3 y 5 insights concretos.
- Mejorar la segmentación según retroalimentación de clase.

---

## Semana 7: Cálculos y analítica intermedia en Tableau

### Objetivo de la semana

Incorporar cálculos analíticos y lógica de negocio dentro del dashboard para pasar de una lectura descriptiva a una lectura más interpretativa.

### Temario desarrollado

- Campos calculados:
  - sintaxis general
  - operaciones numéricas
  - funciones lógicas
  - funciones de fecha
  - funciones de texto
- Métricas derivadas:
  - margen
  - ticket promedio
  - ratio
  - tasa de conversión
  - porcentaje de participación
- Parámetros:
  - selección de medida
  - umbrales
  - escenarios
- Table calculations:
  - percent of total
  - running total
  - moving average
  - rank
  - difference from
- Reference lines, bands y distributions.
- Trend lines y lectura responsable.
- Diferencia entre cálculo a nivel de fila y cálculo a nivel agregado.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de cálculo analítico en visualización
  - errores frecuentes al mezclar agregaciones
- Bloque 2:
  - demostración de campos calculados y parámetros
  - ejercicios con percent of total y running total
- Bloque 3:
  - laboratorio:
    - construir 4 campos calculados
    - agregar una línea de referencia
    - usar una table calculation
    - permitir cambio de métrica vía parámetro
- Bloque 4:
  - revisión de consistencia semántica de los cálculos
  - discusión sobre qué cálculos conviene mostrar y cuáles dejar internos

### Laboratorio sugerido

- Extender el dashboard exploratorio con:
  - métricas derivadas
  - percent of total
  - un parámetro para cambiar medida o periodo
  - una línea de referencia basada en objetivo

### Producto esperado

- Tablero analítico intermedio con mayor expresividad.
- Documento corto de definiciones de métricas.

### Trabajo fuera de clase

- Documentar fórmulas y supuestos.
- Proponer una versión de dashboard para usuario analista y otra para usuario ejecutivo.

---

## Semana 8: Visualización explicativa y storytelling técnico

### Objetivo de la semana

Transformar hallazgos exploratorios en una narrativa visual clara, precisa y defendible técnicamente.

### Temario desarrollado

- Diferencia entre dashboard exploratorio y pieza explicativa.
- Criterios para seleccionar el hallazgo principal.
- Estructura mínima de una historia con datos:
  - contexto
  - pregunta
  - hallazgo
  - evidencia
  - implicancia
  - recomendación
- Redacción de títulos analíticos.
- Uso de subtítulos, captions y notas metodológicas.
- Anotaciones visuales.
- Resaltado visual controlado.
- Secuencia entre vistas en Tableau Story.
- Qué simplificar y qué preservar para no perder rigor.
- Relación entre narrativa y trazabilidad del dato.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría del storytelling técnico
  - análisis de historias bien y mal construidas
- Bloque 2:
  - demostración de anotaciones, captions, tooltips narrativos y Tableau Story
  - transformación de una vista exploratoria en una vista explicativa
- Bloque 3:
  - laboratorio:
    - elegir un hallazgo principal
    - rediseñar 3 a 5 vistas
    - construir secuencia narrativa
    - incorporar texto y anotaciones
- Bloque 4:
  - presentación corta de historias por pares
  - retroalimentación sobre claridad, evidencia y foco

### Laboratorio sugerido

- Crear una historia de Tableau con:
  - portada o contexto
  - dos vistas de evidencia
  - una vista de síntesis
  - una recomendación o conclusión

### Producto esperado

- Historia visual explicativa técnicamente sustentada.

### Trabajo fuera de clase

- Ajustar narrativa y títulos.
- Preparar versión corta de presentación oral de 3 a 5 minutos.

---

## Semana 9: Diseño, accesibilidad y usabilidad de dashboards

### Objetivo de la semana

Mejorar la calidad visual y funcional de dashboards aplicando principios de accesibilidad, jerarquía visual y diseño centrado en el usuario.

### Temario desarrollado

- Percepción visual aplicada a dashboards.
- Principios de preatención:
  - color
  - tamaño
  - posición
  - orientación
- Jerarquía visual.
- Layout y grilla.
- Containers horizontales y verticales en Tableau.
- Espacio en blanco, alineación y consistencia.
- Accesibilidad:
  - contraste
  - tamaño de fuente
  - paletas seguras para daltonismo
  - redundancia visual
- Diseño para distintos dispositivos.
- Legibilidad de etiquetas y tooltips.
- Errores frecuentes:
  - dashboards saturados
  - demasiados filtros
  - color decorativo
  - KPIs sin contexto

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - fundamentos de percepción, accesibilidad y diseño de interfaz visual
  - revisión crítica de dashboards reales
- Bloque 2:
  - demostración de layout con containers, spacing, formato y paletas
  - ajustes de device layout
- Bloque 3:
  - laboratorio de rediseño:
    - reorganizar dashboard existente
    - simplificar elementos
    - mejorar contraste
    - revisar legibilidad
- Bloque 4:
  - checklist de usabilidad y accesibilidad aplicado al tablero
  - priorización de mejoras

### Laboratorio sugerido

- Tomar un dashboard previo y hacer dos versiones:
  - versión original
  - versión optimizada para accesibilidad y claridad

### Producto esperado

- Dashboard rediseñado con mejor jerarquía y menor ruido visual.

### Trabajo fuera de clase

- Aplicar checklist completo de accesibilidad.
- Preparar un before/after explicando cada mejora.

---

## Semana 10: Visualización longitudinal y análisis temporal

### Objetivo de la semana

Analizar fenómenos en el tiempo usando series temporales, comparaciones interperiodo y técnicas de suavizado o tendencia.

### Temario desarrollado

- Naturaleza del dato temporal.
- Tipos de preguntas temporales:
  - evolución
  - crecimiento
  - cambio de tendencia
  - estacionalidad
  - comparación interanual
- Jerarquías de fecha en Tableau:
  - año
  - trimestre
  - mes
  - semana
  - día
- Fechas continuas y discretas.
- Gráficos temporales:
  - líneas
  - áreas
  - dual axis cuando realmente se justifica
  - small multiples temporales
- Moving average.
- Running total.
- Comparison to previous period.
- Forecasting básico en Tableau:
  - utilidad
  - supuestos
  - límites
- Riesgos de interpretación:
  - granularidad errónea
  - ventanas incompletas
  - promedios engañosos

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de series temporales para análisis visual
  - discusión sobre estacionalidad, tendencia y ruido
- Bloque 2:
  - demostración de construcción temporal en Tableau
  - moving average, running total y forecast básico
- Bloque 3:
  - laboratorio:
    - construir varias vistas temporales
    - comparar periodos
    - detectar cambio de tendencia
    - incorporar un cálculo temporal
- Bloque 4:
  - revisión metodológica de interpretaciones temporales
  - selección de la mejor vista temporal para el dashboard final

### Laboratorio sugerido

- Crear un dashboard temporal con:
  - una tendencia principal
  - una comparación entre periodos
  - una métrica acumulada o suavizada
  - una conclusión escrita

### Producto esperado

- Componente temporal sólido para el proyecto final.

### Trabajo fuera de clase

- Refinar títulos temporales.
- Preparar explicación de un patrón detectado y sus límites interpretativos.

---

## Semana 11: Visualización transversal, comparativa y geográfica

### Objetivo de la semana

Comparar grupos, categorías, regiones y segmentos utilizando codificaciones visuales apropiadas para análisis transversal.

### Temario desarrollado

- Qué se entiende por análisis transversal.
- Comparación entre grupos en un mismo corte temporal o lógico.
- Técnicas visuales de comparación:
  - barras ordenadas
  - side-by-side bars
  - heatmaps
  - highlight tables
  - treemaps
  - small multiples
- Cuándo usar mapas y cuándo no.
- Mapas en Tableau:
  - rol geográfico
  - latitud y longitud
  - símbolos
  - mapas rellenos
- Riesgos de visualización geográfica:
  - área engañosa
  - densidad no normalizada
  - falta de contexto poblacional
- Comparaciones multivariadas.
- Diseño de vistas para ranking, participación y composición.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de comparación transversal y geográfica
  - selección de gráfico según tipo de comparación
- Bloque 2:
  - demostración de mapas, heatmaps y highlight tables en Tableau
  - construcción de small multiples
- Bloque 3:
  - laboratorio:
    - comparar segmentos o regiones
    - crear una vista geográfica si el dataset lo permite
    - construir una vista de composición o participación
- Bloque 4:
  - crítica metodológica de mapas creados
  - definición de la vista comparativa que entrará al proyecto final

### Laboratorio sugerido

- Elaborar una vista comparativa transversal con al menos dos dimensiones.
- Si hay datos geográficos, integrar un mapa acompañado de otra vista de contexto.

### Producto esperado

- Módulo comparativo y, si aplica, geográfico para el proyecto final.

### Trabajo fuera de clase

- Revisar si la comparación elegida realmente responde la pregunta analítica.
- Ajustar color y orden para mejorar interpretación.

---

## Semana 12: Técnicas avanzadas de visualización para alta dimensionalidad

### Objetivo de la semana

Introducir técnicas de reducción de dimensionalidad para explorar visualmente datasets complejos, y entender cómo integrar esos resultados en Tableau.

### Temario desarrollado

- Qué significa alta dimensionalidad.
- Problema de visualizar datos con muchas variables.
- Diferencia entre:
  - reducción de dimensionalidad
  - selección de variables
  - agregación
- Introducción conceptual a:
  - `PCA`
  - `t-SNE`
- Qué preserva `PCA` y qué no.
- Qué preserva `t-SNE` y qué no.
- Cuándo tiene sentido usar `t-SNE`:
  - embeddings
  - perfiles de usuarios
  - texto vectorizado
  - imágenes ya embebidas
  - clustering exploratorio
- Riesgos de interpretación de `t-SNE`:
  - distancias globales engañosas
  - sensibilidad a hiperparámetros
  - resultados no deterministas si no se controla semilla
- Pipeline sugerido:
  - preparar variables numéricas
  - escalar
  - calcular `PCA` si hace falta
  - calcular `t-SNE` en Python
  - exportar coordenadas
  - visualizar en Tableau
- Cómo construir un scatter plot de embeddings en Tableau:
  - color por cluster o clase
  - tamaño por variable de interés
  - tooltip enriquecido
  - acciones de highlight
- Relación entre esta técnica y análisis exploratorio avanzado.

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - teoría de reducción de dimensionalidad y advertencias metodológicas
  - comparación conceptual `PCA` vs `t-SNE`
- Bloque 2:
  - demostración técnica del pipeline:
    - preparación de variables
    - cálculo de proyecciones fuera de Tableau
    - carga del resultado en Tableau
- Bloque 3:
  - laboratorio:
    - usar un dataset con varias variables numéricas
    - cargar coordenadas 2D generadas previamente
    - construir scatter plot interpretativo
    - explorar grupos y outliers
- Bloque 4:
  - discusión sobre lo que sí se puede afirmar y lo que no
  - revisión de cómo documentar metodología avanzada en el dashboard

### Laboratorio sugerido

- Dataset con varias variables o embedding precalculado.
- Construir una vista con:
  - eje 1 y eje 2 de `PCA` o `t-SNE`
  - color por categoría
  - tooltip con variables originales
  - filtro por grupo o cluster

### Producto esperado

- Visualización avanzada de proyección de alta dimensionalidad.
- Nota metodológica para evitar sobreinterpretación.

### Trabajo fuera de clase

- Documentar:
  - algoritmo usado
  - variables utilizadas
  - posibles limitaciones interpretativas

---

## Semana 13: Ingeniería de dashboards, interactividad y publicación

### Objetivo de la semana

Integrar visualizaciones en un dashboard robusto, navegable y publicable, cuidando rendimiento, interacción y consistencia de experiencia.

### Temario desarrollado

- Arquitectura de un dashboard final.
- Selección de vistas esenciales vs vistas accesorias.
- Principios de navegación visual.
- Interactividad en Tableau:
  - filter actions
  - highlight actions
  - URL actions
  - parameter actions
- Tooltips enriquecidos y viz in tooltip.
- Diseño orientado a tareas:
  - comparación
  - monitoreo
  - exploración
  - comunicación ejecutiva
- Rendimiento básico:
  - reducir hojas innecesarias
  - controlar granularidad
  - evitar cálculos costosos sin necesidad
  - limitar filtros redundantes
- Publicación:
  - Tableau Public
  - empaquetado del workbook
  - cuidado con datos sensibles
- Comparación corta con Power BI:
  - ventajas y desventajas en publicación, modelado y narrativa

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - diseño de arquitectura final del dashboard
  - checklist de usabilidad y rendimiento
- Bloque 2:
  - demostración de acciones interactivas y publicación
  - ejemplo de dashboard navegable end-to-end
- Bloque 3:
  - laboratorio:
    - ensamblar dashboard final
    - integrar acciones
    - probar recorridos de usuario
    - optimizar layout y carga
- Bloque 4:
  - prueba cruzada entre grupos o compañeros
  - lista final de ajustes antes de entrega

### Laboratorio sugerido

- Construir el dashboard final con:
  - vista resumen
  - vista temporal o comparativa
  - filtro principal
  - una acción interactiva
  - una nota metodológica

### Producto esperado

- Dashboard final navegable y listo para publicación o presentación.

### Trabajo fuera de clase

- Publicar versión candidata.
- Corregir hallazgos de usabilidad y rendimiento.

---

## Semana 14: Proyecto integrador técnico y defensa final

### Objetivo de la semana

Presentar un producto visual completo, justificando tanto las decisiones técnicas sobre datos como las decisiones de diseño y comunicación.

### Temario desarrollado

- Estructura de presentación final:
  - problema
  - datos
  - preparación
  - análisis
  - visualización
  - hallazgos
  - recomendaciones
- Cómo defender decisiones técnicas:
  - por qué ese dataset
  - cómo se limpió
  - cómo se modeló
  - por qué esos gráficos
  - por qué ese dashboard
- Cómo defender decisiones metodológicas:
  - limitaciones del dato
  - sesgos detectados
  - supuestos analíticos
  - límites del forecasting o del `t-SNE` si aplica
- Criterios de evaluación técnica sugeridos:
  - calidad del dato
  - consistencia del modelado
  - validez de los cálculos
  - legibilidad visual
  - interactividad
  - capacidad de síntesis
- Criterios de evaluación de comunicación:
  - claridad del problema
  - solidez del insight
  - coherencia narrativa
  - utilidad de la recomendación

### Desarrollo de la sesión de 4 horas

- Bloque 1:
  - organización final del flujo de defensa
  - revisión de checklist técnico antes de presentar
- Bloque 2:
  - ajuste final del dashboard y de la secuencia de exposición
- Bloque 3:
  - presentación de proyectos
  - preguntas técnicas y metodológicas
- Bloque 4:
  - retroalimentación final
  - cierre del curso y recomendaciones para portafolio

### Laboratorio sugerido

- Presentación final del dashboard o historia visual.
- Defensa del pipeline completo:
  - perfilado
  - limpieza
  - transformación
  - análisis
  - diseño
  - publicación

### Producto esperado

- Entrega final del proyecto técnico de visualización.
- Presentación oral breve con defensa analítica y visual.

### Trabajo fuera de clase

- Dejar versión final publicada o empaquetada.
- Preparar una versión portafolio con mejor narrativa y estética.

---

## Recomendaciones de implementación docente

- Mantener un único dataset base durante buena parte del curso para que la complejidad esté en el análisis y no en el cambio constante de contexto.
- Usar `Tableau` como herramienta principal en todas las evaluaciones para consolidar habilidades.
- Reservar `Power BI` solo para comparación puntual y no como eje paralelo del curso.
- Introducir `Python` solo cuando aporte valor directo:
  - limpieza compleja
  - cálculo de `PCA`
  - cálculo de `t-SNE`
- Pedir documentación mínima de todo cambio en los datos para reforzar trazabilidad.
- Evaluar no solo el resultado visual, sino también la corrección del pipeline técnico.

## Entregables sugeridos durante el ciclo

- Semana 2: perfil técnico del dataset.
- Semana 3: bitácora de limpieza y dataset depurado.
- Semana 4: fuente modelada y validada.
- Semana 6: dashboard exploratorio inicial.
- Semana 7: tablero con cálculos analíticos.
- Semana 8: historia visual explicativa.
- Semana 10: componente temporal bien argumentado.
- Semana 12: visualización avanzada con `PCA` o `t-SNE`.
- Semana 13: dashboard final publicable.
- Semana 14: proyecto integrador y defensa final.
