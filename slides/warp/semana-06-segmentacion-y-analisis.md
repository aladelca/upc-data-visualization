# Semana 6: Segmentacion, comparaciones condicionales e interpretacion

## Slide 1. Proposito de la semana

- Pasar de exploracion general a analisis segmentado.
- Usar filtros, bins, groups y sets con criterio analitico.
- Escribir hallazgos basados en evidencia visual y no en intuiciones.

---

## Slide 2. Fundamento teorico

- Analizar es introducir comparaciones controladas.
- La segmentacion divide el espacio de observacion para volver visibles diferencias relevantes.
- Correlacion visual no equivale a causalidad:
  - puede sugerir patron
  - no prueba mecanismo

---

## Slide 3. Logica de segmentacion

![Segmentation logic](./assets/segmentation-analysis.svg)

- `Groups` condensan categorias semanticamente cercanas.
- `Bins` discretizan continuas para observar distribucion o comportamiento por rangos.
- `Sets` separan miembros relevantes del resto.
- Los filtros cambian el universo analizado y por eso alteran toda interpretacion posterior.

---

## Slide 4. Tecnicas en Tableau

- Filtros:
  - quick filters
  - context filters
  - filtros por medida y dimension
- Segmentacion:
  - groups
  - sets
  - bins
- Analisis:
  - highlight
  - drill-down
  - comparaciones top vs rest

---

## Slide 5. Escritura de insights

- Un insight util debe tener:
  - sujeto
  - hallazgo
  - evidencia
  - implicancia
- Formula recomendada:
  - "En el segmento X, la metrica Y aumenta/disminuye Z respecto al segmento W, lo que sugiere..."
- Evitar:
  - interpretaciones causales
  - afirmaciones sin contraste
  - lenguaje ambiguo

---

## Slide 6. Laboratorio guiado

1. Crear un dashboard exploratorio con 3 a 4 vistas.
2. Agregar:
   - un filtro relevante
   - un set o group
   - un bin si hay variable continua
3. Redactar tres insights sostenidos por ese dashboard.

---

## Slide 7. Errores frecuentes

- Filtrar hasta destruir contexto.
- Crear segmentos solo porque el software lo permite.
- Usar correlacion visual como si fuera explicacion causal.
- Escribir insight que solo describe un grafico sin agregar interpretacion.

---

## Slide 8. Referencias

- Few, *Now You See It*
- Munzner, *Visualization Analysis and Design*
- Knaflic, *Storytelling with Data*

