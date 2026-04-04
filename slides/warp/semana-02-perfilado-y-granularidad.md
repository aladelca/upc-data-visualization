# Semana 2: Perfilado del dato, granularidad y lectura estructural

## Slide 1. Proposito de la semana

- Comprender la estructura tecnica del dataset antes de visualizar.
- Identificar unidad de analisis, granularidad, tipos de variables y riesgos de calidad.
- Traducir el perfilado del dato en decisiones visuales y analiticas.

---

## Slide 2. Marco teorico

- Toda visualizacion valida depende de una correcta lectura estructural del dato.
- Un mismo dataset puede permitir o bloquear ciertas preguntas segun su granularidad.
- En terminos teoricos, perfilar significa describir:
  - cobertura
  - completitud
  - consistencia
  - variabilidad
  - plausibilidad

---

## Slide 3. Conceptos que deben quedar fijados

- Unidad de analisis:
  - que representa cada fila
- Granularidad:
  - nivel de detalle del registro
- Tipo de variable:
  - nominal, ordinal, discreta, continua, temporal, geografica
- Jerarquia:
  - fecha, region, producto, organizacion
- Riesgo clasico:
  - visualizar una agregacion cuando el dato subyacente no la soporta semanticamente

---

## Slide 4. Pipeline de calidad y lectura estructural

![Pipeline de calidad](./assets/data-quality-pipeline.svg)

- El perfilado no es limpieza todavia.
- Primero se observa, luego se diagnostica y recien despues se interviene.
- Una visualizacion honesta exige explicitar que campos son completos, comparables y confiables.

---

## Slide 5. Perfilado tecnico en Tableau

- Revisar conteo total de registros.
- Medir cardinalidad por columna.
- Detectar:
  - porcentaje de nulos
  - campos mal inferidos
  - fechas invalidas
  - formatos mixtos
  - categorias sospechosas
- Evaluar si la fuente responde preguntas de:
  - comparacion
  - tendencia
  - relacion
  - composicion

---

## Slide 6. Laboratorio guiado

1. Identificar la unidad de analisis exacta del dataset.
2. Construir una tabla de perfilado con:
   - nombre de columna
   - tipo esperado
   - tipo actual
   - nulos
   - cardinalidad
   - observaciones
3. Detectar al menos tres problemas que afectarian una visualizacion futura.

---

## Slide 7. Criterios teoricos para interpretar el perfilado

- Alta cardinalidad no implica automaticamente mayor valor analitico.
- Un campo fecha mal formado destruye cualquier lectura longitudinal.
- Un campo categorico sucio distorsiona rankings y comparaciones.
- Los nulos pueden ser:
  - ausencia real
  - error de captura
  - dato no aplicable
  - dato censurado

---

## Slide 8. Referencias

- Knaflic, *Storytelling with Data*
- Munzner, *Visualization Analysis and Design*
- Wickham, *Tidy Data*

