---
marp: true
theme: gaia
paginate: true
size: 16:9
title: Semana 10 - Series temporales
description: Tendencia, estacionalidad, comparacion y forecasting basico
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
# Semana 10
## Visualizacion longitudinal y analisis temporal

- El tiempo no es solo una variable mas: impone orden, continuidad y comparabilidad
- Meta: construir lecturas temporales defendibles

---

## Objetivos de la semana

- Diferenciar tendencia, estacionalidad, ruido y quiebre.
- Usar granularidad temporal correcta.
- Aplicar `running total`, `moving average` y comparaciones interperiodo.

---

## Agenda sugerida de las 4 horas

| Tramo | Tiempo | Actividad |
|---|---:|---|
| Apertura | 0:00 - 0:20 | Recap del rediseño y pregunta temporal del dia |
| Teoria | 0:20 - 1:15 | Serie temporal, tendencia, estacionalidad y forecast |
| Demo | 1:15 - 2:00 | Fechas, `moving average`, `running total` y comparaciones en Tableau |
| Laboratorio | 2:00 - 3:25 | Dashboard temporal con insight y advertencia metodologica |
| Cierre | 3:25 - 4:00 | Discusion sobre limites del forecasting visual |

---

## Fundamento teorico

- Una serie temporal exige preservar:
  - orden
  - ventana
  - escala
  - periodicidad
- La mala visualizacion temporal suele nacer de:
  - granularidad mezclada
  - ventanas incompletas
  - comparaciones no homologas

---

## Marco de lectura temporal

![Time series frame](./assets/time-series-analysis.svg)

- La serie observada combina señal y ruido.
- El suavizado ayuda a leer patron, pero no reemplaza al dato observado.

---

## Descomposicion temporal

![Forecast decomposition](./assets/forecast-decomposition.svg)

- Elementos clasicos:
  - observacion
  - tendencia
  - estacionalidad
  - residual
- Esta distincion mejora tanto la lectura como el reporte de hallazgos.

---

## Tecnicas en Tableau

- Fechas continuas vs discretas.
- Jerarquias temporales.
- `Running total`.
- `Moving average`.
- Comparacion con periodo previo.
- Forecasting basico con advertencia metodologica.

---

## Criterios teoricos

- Una tendencia sostenida no se infiere por un solo punto extremo.
- Estacionalidad no debe confundirse con crecimiento estructural.
- Un forecast en Tableau es orientativo, no evidencia causal ni pronostico robusto por si solo.

---

## Preguntas temporales canonicas

- Que tan rapido cambia?
- El cambio es sostenido o puntual?
- Existen ciclos repetitivos?
- El comportamiento reciente contradice el historico?
- Hay quiebres luego de un evento o intervencion?

---

## Fallos interpretativos comunes

- Comparar periodos con distinta longitud.
- Ignorar rezagos.
- Leer ruido como señal.
- Confundir recuperacion temporal con cambio estructural.
- Inferir causalidad por coincidencia temporal.

---

## Laboratorio guiado

1. Construir una vista temporal principal.
2. Agregar una comparacion interperiodo.
3. Crear una metrica acumulada o suavizada.
4. Redactar un insight temporal y su limitacion.

---

## Errores frecuentes

- Comparar meses parciales con meses completos.
- Usar dual axis sin razon clara.
- Elegir una granularidad que oculta el fenomeno.
- Tomar el forecast como prediccion final.

---

## Preguntas para clase

- Que seria una buena linea base para comparar esta serie?
- Que evento externo podria explicar un quiebre sin que la vista lo pruebe?
- Que parte de la serie necesitaria mas contexto antes de concluir algo?

---

## Referencias

- Few, *Now You See It*
- Kirk, *Data Visualisation*
- Cairo, *How Charts Lie*
