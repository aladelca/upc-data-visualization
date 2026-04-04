# Semana 4: Modelado de fuentes y preparacion analitica

## Slide 1. Proposito de la semana

- Construir una fuente analitica util para Tableau.
- Distinguir joins, unions, relationships y blending.
- Validar que el modelo no introduzca duplicaciones o errores semanticos.

---

## Slide 2. Fundamento teorico

- Visualizar no es solo dibujar; es tambien modelar bien la estructura relacional del dato.
- Un dashboard puede ser visualmente correcto y logicamente falso si el join esta mal planteado.
- El criterio central es preservar cardinalidad, sentido de los totales y coherencia entre dimensiones y medidas.

---

## Slide 3. Vocabulario minimo de modelado

| Concepto | Uso principal | Riesgo tipico |
|---|---|---|
| Join | Combinar tablas por clave | Duplicacion por cardinalidad |
| Union | Apilar tablas equivalentes | Esquema inconsistente |
| Relationship | Relacion flexible en Tableau | Falsa seguridad si no se valida |
| Blending | Cruce tardio entre fuentes | Errores de nivel de detalle |

---

## Slide 4. Esquema analitico para visualizacion

![Modelo analitico](./assets/tableau-data-model.svg)

- El modelo de trabajo ideal separa eventos o hechos de dimensiones de contexto.
- Conviene pensar la fuente como una mini estrella analitica:
  - hecho central
  - tiempo
  - producto
  - cliente
  - region

---

## Slide 5. Validaciones obligatorias

- Conteo de registros antes y despues del join.
- Totales de medidas criticas antes y despues del modelado.
- Verificacion de claves unicas.
- Identificacion de relaciones:
  - uno a uno
  - uno a muchos
  - muchos a muchos
- Creacion de campos calculados basicos:
  - margen
  - tasa
  - porcentaje
  - indicador logico

---

## Slide 6. Laboratorio guiado

1. Unir o relacionar dos tablas.
2. Crear una jerarquia temporal o geografica.
3. Generar tres campos calculados basicos.
4. Validar:
   - conteos
   - totales
   - consistencia de agregacion

---

## Slide 7. Anti patrones que deben evitarse

- Hacer joins sin conocer cardinalidad.
- Mezclar medidas con diferente nivel de detalle.
- Confiar en relationships sin validar resultados numericos.
- Agregar demasiado pronto y perder capacidad exploratoria.
- Modelar para "que funcione" y no para que sea interpretable.

---

## Slide 8. Referencias

- Munzner, *Visualization Analysis and Design*
- Kimball, *The Data Warehouse Toolkit*
- Tableau Help, modelado de datos y relaciones

