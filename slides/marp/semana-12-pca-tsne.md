---
marp: true
theme: gaia
paginate: true
size: 16:9
title: Semana 12 - PCA y t-SNE
description: Visualizacion de alta dimensionalidad
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
# Semana 12
## Visualizacion de alta dimensionalidad con PCA y t-SNE

- `PCA` y `t-SNE` no son graficos: son transformaciones del espacio de datos
- Meta: integrar proyecciones externas en Tableau con interpretacion responsable

---

## Objetivos de la semana

- Comprender la logica de reduccion de dimensionalidad.
- Distinguir preservacion global (`PCA`) de preservacion local (`t-SNE`).
- Visualizar embeddings o proyecciones en Tableau.

---

## Agenda sugerida de las 4 horas

| Tramo | Tiempo | Actividad |
|---|---:|---|
| Apertura | 0:00 - 0:20 | Recap comparativo y motivacion de alta dimensionalidad |
| Teoria | 0:20 - 1:15 | `PCA`, `t-SNE`, preservacion local/global y limites |
| Demo | 1:15 - 2:00 | Pipeline de calculo externo y carga en Tableau |
| Laboratorio | 2:00 - 3:25 | Scatter de proyeccion, clusters y tooltip contextual |
| Cierre | 3:25 - 4:00 | Debate sobre sobreinterpretacion y trazabilidad metodologica |

---

## Fundamento teorico

- Cuando las variables son muchas, el espacio deja de ser intuitivo.
- La reduccion de dimensionalidad busca representar estructura en menor numero de ejes.
- Dos advertencias:
  - toda proyeccion pierde informacion
  - lo que se preserva depende del algoritmo

---

## `PCA` vs `t-SNE`

| Tecnica | Tipo | Lo que prioriza | Riesgo |
|---|---|---|---|
| `PCA` | Lineal | Varianza global | Perder estructura no lineal |
| `t-SNE` | No lineal | Vecindad local | Sobreinterpretar distancia global |

- `PCA` produce componentes interpretables como combinaciones lineales.
- `t-SNE` no produce ejes semanticamente interpretables en sentido tradicional.

---

## Pipeline recomendado

![t-SNE pipeline](./assets/tsne-pipeline.svg)

- Escalar variables.
- Reducir ruido si hace falta.
- Calcular proyeccion fuera de Tableau.
- Exportar coordenadas 2D.
- Visualizar y anotar dentro de Tableau.

---

## Criterios de interpretacion

- En `PCA`, leer cargas y varianza explicada.
- En `t-SNE`, leer vecindad local con prudencia.
- No afirmar cluster "real" solo por una nube visual atractiva.
- Documentar:
  - variables usadas
  - escalado
  - algoritmo
  - hiperparametros

---

## Integracion con Tableau

- Columnas minimas:
  - `x_pca` / `y_pca` o `x_tsne` / `y_tsne`
- Codificaciones sugeridas:
  - color por clase o cluster
  - tamaño por importancia
  - tooltip con variables originales
- Valor didactico:
  - Tableau consume el resultado y facilita inspeccion visual.

---

## Preprocesamiento que no debe omitirse

- Seleccion de variables relevantes.
- Escalado o estandarizacion.
- Tratamiento de nulos.
- Reduccion previa con `PCA` si la dimension es muy alta.
- Control de semilla para reproducibilidad.

---

## Sensibilidad y estabilidad en `t-SNE`

- Cambiar `perplexity` puede alterar la forma.
- Cambiar semilla puede mover estructuras.
- El algoritmo no garantiza una representacion unica.
- Por eso conviene:
  - comparar corridas
  - documentar parametros
  - no sobreafirmar cluster "natural"

---

## Laboratorio guiado

1. Cargar coordenadas precalculadas.
2. Construir scatter plot.
3. Colorear por segmento.
4. Identificar agrupamientos y puntos frontera.
5. Redactar advertencia metodologica.

---

## Errores frecuentes

- Interpretar cada eje de `t-SNE` como variable original.
- Ignorar sensibilidad a semilla o `perplexity`.
- Usar la proyeccion como evidencia final de causalidad o segmentacion definitiva.

---

## Preguntas para clase

- Que preserva `PCA` que `t-SNE` no prioriza?
- Que afirmacion seria legitima al ver dos grupos separados?
- Como explicarias esta vista a alguien no tecnico sin engañarlo?

---

## Referencias

- van der Maaten y Hinton, *Visualizing Data using t-SNE*
- Jolliffe, *Principal Component Analysis*
- Cairo, *How Charts Lie*
