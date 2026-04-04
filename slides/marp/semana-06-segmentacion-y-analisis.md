---
marp: true
theme: gaia
paginate: true
size: 16:9
title: Semana 6 - Segmentacion y analisis
description: Filtros, grupos, bins y escritura de insights
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
# Semana 6
## Segmentacion, comparaciones condicionales e insights

- El analisis mejora cuando comparamos subconjuntos con criterio
- Meta: pasar de vistas generales a hallazgos segmentados

---

## Objetivos de la semana

- Usar `filters`, `groups`, `sets` y `bins` con sentido analitico.
- Diferenciar observacion simple de insight util.
- Construir un dashboard exploratorio con segmentacion controlada.

---

## Agenda sugerida de las 4 horas

| Tramo | Tiempo | Actividad |
|---|---:|---|
| Apertura | 0:00 - 0:20 | Recap del workbook exploratorio y objetivos del dia |
| Teoria | 0:20 - 1:10 | Segmentacion, comparaciones condicionales e insight writing |
| Demo | 1:10 - 2:00 | `Filters`, `bins`, `groups`, `sets` y highlights en Tableau |
| Laboratorio | 2:00 - 3:25 | Dashboard exploratorio segmentado e insights escritos |
| Cierre | 3:25 - 4:00 | Discusion sobre correlacion, causalidad y riesgo inferencial |

---

## Fundamento teorico

- Analizar significa introducir comparaciones relevantes.
- La segmentacion vuelve visibles heterogeneidades que el agregado total oculta.
- Advertencia central:
  - correlacion visual no implica causalidad
  - pero puede sugerir patrones que merecen investigarse

---

## Logica de segmentacion

![Segmentation](./assets/segmentation-analysis.svg)

- `Groups`: condensan categorias semanticamente proximas.
- `Bins`: discretizan variables continuas.
- `Sets`: separan miembros relevantes del resto.
- `Filters`: alteran el universo observado y, por tanto, la interpretacion.

---

## De observacion a insight

![Insight ladder](./assets/insight-ladder.svg)

- Una vista produce observaciones.
- Varias observaciones comparadas producen patrones.
- Los patrones interpretados y conectados con una decision producen insights.

---

## Escritura de insights

- Formula recomendada:
  - **En el segmento X, la metrica Y cambia Z frente a W, lo que sugiere...**
- Componentes minimos:
  - sujeto
  - comparacion
  - evidencia
  - implicancia
- Un buen insight no describe el grafico: interpreta su relevancia.

---

## Criterios para una buena segmentacion

- Relevancia sustantiva:
  - el segmento debe responder una pregunta real
- Estabilidad:
  - no debe depender de una separacion arbitraria
- Interpretabilidad:
  - el lector debe entender por que existe
- Accionabilidad:
  - debe habilitar una decision o una investigacion posterior

---

## Rubrica rapida para evaluar un insight

| Criterio | Bajo | Medio | Alto |
|---|---|---|---|
| Evidencia | Describe sin comparar | Compara parcialmente | Compara con claridad |
| Precision | Vaga | Parcial | Cuantificada |
| Implicancia | Ausente | Sugiere | Conecta con decision |
| Honestidad | Sobreinterpreta | Dudosa | Reconoce limites |

---

## Tecnicas en Tableau

- Quick filters y context filters.
- `Bins` para ingresos, edad, ticket o tiempo de permanencia.
- `Groups` para consolidar categorias.
- `Sets` para top vs rest, segmento critico vs resto.
- Highlight y drill-down para inspeccion puntual.

---

## Laboratorio guiado

1. Crear un dashboard con 3 o 4 vistas.
2. Agregar:
   - un filtro relevante
   - un set o group
   - un bin si el dato lo permite
3. Redactar tres insights apoyados por evidencia.

---

## Errores frecuentes

- Filtrar hasta perder contexto.
- Segmentar por variables irrelevantes.
- Llamar insight a cualquier observacion visual.
- Hacer afirmaciones causales a partir de un scatter.

---

## Preguntas para cierre de clase

- Que segmento revela mayor heterogeneidad y por que?
- Cual de tus insights podria defenderse ante un gerente?
- Que insight necesita evidencia adicional antes de presentarse como conclusion?

---

## Referencias

- Few, *Now You See It*
- Munzner, *Visualization Analysis and Design*
- Knaflic, *Storytelling with Data*
