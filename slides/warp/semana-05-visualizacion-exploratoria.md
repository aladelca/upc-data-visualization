# Semana 5: Visualizacion exploratoria y seleccion de graficos

## Slide 1. Proposito de la semana

- Seleccionar graficos en funcion de la pregunta analitica.
- Aplicar principios perceptuales para comparacion, distribucion, relacion y tiempo.
- Construir el primer workbook exploratorio coherente.

---

## Slide 2. Fundamento teorico

- Cleveland y McGill demostraron que no todas las codificaciones visuales tienen la misma precision perceptual.
- Jerarquia perceptual clave:
  - posicion comun
  - longitud
  - angulo
  - area
  - color
- En consecuencia, la seleccion de graficos no es estetica: es una decision epistemica.

---

## Slide 3. Matriz de seleccion

![Chart selection](./assets/chart-selection.svg)

- Comparar:
  - barras, dot plots, rankings
- Distribuir:
  - histogramas, boxplots, densidad
- Relacionar:
  - dispersion, matrices, heatmaps
- Temporalidad:
  - linea, area, small multiples

---

## Slide 4. Reglas teoricas por familia de grafico

- Barras:
  - usar cuando la comparacion entre categorias es central
  - ordenar para facilitar lectura
- Histogramas:
  - sirven para forma y dispersion, no para detalle individual
- Boxplots:
  - resumen robusto de distribucion y outliers
- Scatter plots:
  - revelan relacion, clusters y anomalías
- Lineas:
  - privilegian continuidad temporal

---

## Slide 5. Construccion tecnica en Tableau

- Hojas minimas de esta semana:
  - comparacion por categoria
  - distribucion de una variable
  - evolucion temporal basica
  - relacion entre dos variables
  - ranking top N
- Ajustes obligatorios:
  - titulos informativos
  - orden correcto
  - formatos numericos consistentes
  - tooltips legibles

---

## Slide 6. Laboratorio guiado

1. Construir 5 vistas exploratorias.
2. Elegir para cada una la pregunta analitica que responde.
3. Justificar por que otra codificacion seria inferior.
4. Detectar una vista innecesaria y reemplazarla por una mas precisa.

---

## Slide 7. Errores frecuentes

- Usar pastel para muchas categorias.
- Codificar magnitud con area cuando la comparacion exige posicion o longitud.
- Saturar de color sin semantica.
- Mantener orden alfabetico cuando el analitico deberia ser por valor.
- Construir varias vistas redundantes que responden la misma pregunta.

---

## Slide 8. Referencias

- Cleveland, *The Elements of Graphing Data*
- Few, *Show Me the Numbers*
- Cairo, *The Functional Art*

