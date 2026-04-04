---
marp: true
theme: gaia
paginate: true
size: 16:9
title: Semana 5 - Visualizacion exploratoria
description: Seleccion de graficos y primeras vistas analiticas
style: |
  section {
    font-family: Aptos, "Segoe UI", Arial, sans-serif;
    background: #f3f4f6;
    color: #111111;
    padding: 52px 60px;
    font-size: 26px;
    line-height: 1.34;
  }
  section.lead {
    background: linear-gradient(135deg, #0b0b0c 0%, #2f2f33 100%);
    color: #ffffff;
  }
  section.lead h1, section.lead h2, section.lead h3, section.lead p, section.lead li { color: #ffffff; }
  h1, h2, h3 { color: #111111; }
  h1 { font-size: 1.56em; border-left: 10px solid #6b7280; padding-left: 16px; letter-spacing: 0.01em; }
  section.lead h1 { border-left-color: rgba(255,255,255,0.65); }
  h2 { font-size: 1.14em; color: #3f3f46; }
  h3 { color: #52525b; }
  ul, ol { padding-left: 1.05em; }
  img { display: block; margin: 0 auto; max-width: 100%; max-height: 420px; border-radius: 14px; box-shadow: 0 16px 32px rgba(0,0,0,0.14); background: #ffffff; filter: grayscale(100%); }
  table { font-size: 0.70em; border-collapse: collapse; background: #ffffff; }
  th { background: #18181b; color: #ffffff; }
  th, td { padding: 8px 12px; border: 1px solid #d4d4d8; }
  strong { color: #27272a; font-weight: 700; }
  code { background: #e5e7eb; color: #111111; padding: 0.08em 0.28em; border-radius: 6px; }
  blockquote { border-left: 8px solid #71717a; padding-left: 16px; color: #3f3f46; }
---

<!-- _class: lead -->
# Semana 5
## Visualizacion exploratoria y seleccion de graficos

- La eleccion del grafico no es estetica: es una hipotesis sobre como leer mejor el dato
- Meta: construir un workbook exploratorio base

---

## Objetivos de la semana

- Aplicar reglas de seleccion de graficos segun la tarea analitica.
- Usar principios perceptuales de Cleveland y McGill.
- Producir un conjunto coherente de hojas exploratorias.

---

## Agenda sugerida de las 4 horas

| Tramo | Tiempo | Actividad |
|---|---:|---|
| Apertura | 0:00 - 0:20 | Recap de modelado y pregunta analitica dominante |
| Teoria | 0:20 - 1:10 | Jerarquia perceptual y seleccion de graficos |
| Demo | 1:10 - 2:00 | Construccion guiada de barras, histogramas, scatter y lineas |
| Laboratorio | 2:00 - 3:25 | Workbook exploratorio con cinco hojas y justificacion |
| Cierre | 3:25 - 4:00 | Critica cruzada y descarte de vistas debiles |

---

## Fundamento teorico

- Las codificaciones visuales no tienen la misma precision.
- Jerarquia perceptual simplificada:
  - posicion comun
  - longitud
  - angulo
  - area
  - color
- Consecuencia:
  - para comparar magnitudes, preferir barras o dot plots antes que pastel o burbujas.

---

## Matriz de seleccion de graficos

![Chart selection](./assets/chart-selection.svg)

- Comparacion -> barras, puntos, rankings
- Distribucion -> histogramas, boxplots
- Relacion -> dispersion, matrices
- Tiempo -> lineas, areas, small multiples

---

## Reglas teoricas por familia

- **Barras**: alta precision para ranking y comparacion categorial.
- **Histogramas**: revelan forma, dispersion y asimetria.
- **Boxplots**: resumen robusto y detection de outliers.
- **Scatter**: relacion, cluster, heterogeneidad.
- **Lineas**: cambio continuo en el tiempo.

---

## Como pensar la exploracion

- Explorar no es producir muchos graficos.
- Explorar bien exige:
  - preguntas concretas
  - iteracion rapida
  - comparaciones controladas
  - descarte de vistas redundantes
- Una buena hoja exploratoria deja claro:
  - que compara
  - a que escala
  - con que agregado

---

## Integridad visual: chart junk y distorsion

- Evitar:
  - 3D
  - sombras innecesarias
  - iconografia decorativa
  - leyendas redundantes
  - ejes truncados sin advertencia
- Principio:
  - si un elemento visual no mejora comprension, probablemente introduce ruido.

---

## Tabla de mapeo pregunta -> grafico

| Pregunta | Vista recomendada | Vista a evitar |
|---|---|---|
| Quien vende mas? | Barras ordenadas | Pie chart |
| Como se distribuye el ingreso? | Histograma / boxplot | Tabla sin resumen |
| Hay relacion entre precio y margen? | Scatter | Dos barras separadas |
| Como cambia por mes? | Linea | Barras desordenadas |

---

## Construccion tecnica en Tableau

- Hojas minimas:
  - comparacion categorial
  - distribucion
  - tendencia
  - relacion entre dos variables
  - ranking top N
- Ajustes obligatorios:
  - orden intencional
  - titulos claros
  - formato de ejes
  - tooltips sin ruido

---

## Laboratorio guiado

1. Construir al menos cinco hojas.
2. Nombrarlas segun la pregunta que responden.
3. Justificar verbalmente la codificacion elegida.
4. Descartar una vista innecesaria y reemplazarla por una mejor.

---

## Errores frecuentes

- Pie charts con demasiadas categorias.
- Demasiados colores sin semantica.
- Ejes truncados sin justificacion.
- Orden alfabetico donde deberia haber ranking.
- Varias vistas que responden la misma pregunta.

---

## Preguntas para discusion

- Que grafico elegirias si necesitas comparar 30 categorias?
- Cuando una tabla puede ser superior a un grafico?
- Que diferencia hay entre una vista para descubrir y una vista para demostrar?

---

## Referencias

- Cleveland, *The Elements of Graphing Data*
- Few, *Show Me the Numbers*
- Cairo, *The Functional Art*
