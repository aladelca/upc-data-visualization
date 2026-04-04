# Semana 3: Limpieza y preparacion de datos

## Slide 1. Proposito de la semana

- Entender la limpieza como condicion epistemica de la visualizacion, no como tarea cosmetica.
- Corregir tipos, nulos, categorias y formatos.
- Dejar una bitacora reproducible de toda intervencion.

---

## Slide 2. Fundamento teorico

- Una visualizacion nunca es mejor que los supuestos que incorpora.
- Limpiar es decidir:
  - que se corrige
  - que se excluye
  - que se conserva con advertencia
- Segun Wickham, preparar bien los datos reduce friccion analitica y mejora consistencia semantica.

---

## Slide 3. Tipologia de problemas de limpieza

- Tipos mal inferidos:
  - texto que deberia ser fecha o numero
- Valores faltantes:
  - nulo tecnico vs ausencia informativa
- Categorias inconsistentes:
  - abreviaciones, errores de digitacion, sinonimos
- Duplicados:
  - exactos o funcionales
- Formatos heterogeneos:
  - moneda, porcentaje, fecha, codigo

---

## Slide 4. Pipeline de intervencion

![Pipeline de calidad](./assets/data-quality-pipeline.svg)

- Perfilar no basta: hay que intervenir con criterio.
- Toda limpieza debe respetar el significado analitico del dato.
- Si la limpieza altera la interpretacion, debe quedar documentado.

---

## Slide 5. Tecnicas concretas

- En Tableau:
  - renombrado de campos
  - aliases
  - split y custom split
  - pivot y unpivot
  - cambio de tipo
- Fuera de Tableau, si hace falta:
  - normalizacion en Excel
  - limpieza reproducible con Python y `pandas`
- Regla metodologica:
  - preferir transformaciones transparentes sobre arreglos manuales invisibles

---

## Slide 6. Laboratorio guiado

1. Corregir tipos de dato.
2. Consolidar categorias duplicadas o inconsistentes.
3. Revisar nulos y decidir:
   - excluir
   - imputar
   - etiquetar
4. Generar una bitacora con:
   - problema
   - accion tomada
   - justificacion
   - impacto esperado

---

## Slide 7. Advertencias teoricas

- Imputar sin criterio puede fabricar patrones que el dato no tenia.
- Eliminar outliers antes de entenderlos puede ocultar hallazgos reales.
- Fusionar categorias sin justificar puede borrar estructura relevante.
- No toda limpieza mejora el analisis: algunas intervenciones lo sesgan.

---

## Slide 8. Referencias

- Hadley Wickham, *Tidy Data*
- Knaflic, *Storytelling with Data*
- Few, *Show Me the Numbers*

