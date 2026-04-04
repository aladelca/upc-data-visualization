---
marp: true
theme: gaia
paginate: true
size: 16:9
title: Semana 1 - Introduccion tecnica al curso
description: Data Visualization con Tableau
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
# Semana 1
## Introduccion tecnica al curso y ecosistema de visualizacion

- Enfoque del curso: `Tableau` como herramienta principal
- Horizonte metodologico: datos -> estructura -> analisis -> visualizacion -> decision
- Meta de hoy: instalar, conectar, comprender el flujo de trabajo completo

---

## Resultados de aprendizaje de la semana

- Distinguir entre **visualizacion exploratoria**, **visualizacion explicativa** y **storytelling**.
- Comprender por que la visualizacion no es una capa decorativa sino una capa de razonamiento.
- Configurar el entorno de trabajo en `Tableau Desktop` o `Tableau Public`.
- Conectar una fuente real y construir las primeras dos hojas analiticas.

---

## Agenda sugerida de las 4 horas

| Tramo | Tiempo | Actividad |
|---|---:|---|
| Apertura | 0:00 - 0:25 | Presentacion del curso, expectativas y stack tecnico |
| Marco teorico | 0:25 - 1:05 | Rol de la visualizacion, tipos de trabajo visual, criterios de calidad |
| Demo guiada | 1:05 - 2:00 | Instalacion, interfaz de Tableau y conexion a datos |
| Laboratorio | 2:00 - 3:25 | Primer workbook con dos hojas basicas |
| Cierre | 3:25 - 4:00 | Discusion, errores comunes y encargo |

---

## Tesis central de la asignatura

- La visualizacion **no reemplaza** al analisis: lo externaliza y lo vuelve inspeccionable.
- Una visualizacion de calidad requiere coherencia entre:
  - pregunta analitica
  - estructura del dato
  - codificacion visual
  - interaccion
  - contexto de uso
- Si cualquiera de esas capas falla, el dashboard puede verse bien y aun asi inducir errores.

---

## Marco teorico minimo

| Autor | Aporte clave | Implicancia para el curso |
|---|---|---|
| Munzner | Modelo de tareas, datos y codificaciones | Elegir graficos por pregunta y estructura |
| Ware | Percepcion visual y atencion | Disenar para lectura eficiente |
| Few | Precision y simplicidad analitica | Evitar ruido visual y decoracion innecesaria |
| Knaflic | Narrativa basada en evidencia | Convertir hallazgos en mensajes accionables |

---

## Ecosistema de herramientas del curso

![Ecosistema](./assets/tableau-powerbi-ecosystem.svg)

- `Tableau`: exploracion veloz, dashboards, historias, narrativa visual.
- `Power BI`: referencia comparativa para reporting y ecosistema Microsoft.
- `Python`: apoyo puntual para limpieza compleja, `PCA`, `t-SNE` o preparacion avanzada.

---

## Arquitectura conceptual de Tableau

- **Data Source**: define conexion, tipo de fuente, `extract` o `live`.
- **Worksheet**: unidad minima de analisis visual.
- **Dashboard**: composicion de varias vistas en una interfaz unica.
- **Story**: secuencia narrativa de vistas.
- Componentes criticos:
  - `Data pane`
  - `Rows` / `Columns`
  - `Marks`
  - `Filters`
  - `Show Me`

---

## Flujo de trabajo que seguiremos durante el ciclo

1. Perfilar datos y entender granularidad.
2. Limpiar y documentar.
3. Modelar relaciones y validar totales.
4. Construir vistas exploratorias.
5. Pasar a un dashboard explicativo.
6. Publicar y defender decisiones tecnicas.

- Este flujo es acumulativo: una mala etapa temprana contamina todo lo demas.

---

## Por que fallan tantos dashboards en la practica

- Porque se construyen desde la herramienta y no desde la pregunta.
- Porque privilegian abundancia de componentes sobre claridad inferencial.
- Porque mezclan:
  - multiples niveles de detalle
  - metricas mal definidas
  - colores sin semantica
  - interacciones innecesarias
- Porque nadie documenta supuestos de datos, filtros y calculos.

---

## Preguntas guia para discusion en clase

- Que diferencia hay entre una visualizacion "bonita" y una visualizacion "util"?
- Cuando una tabla supera a un grafico?
- En que tipo de decisiones un dashboard puede inducir error si no explicita contexto?
- Que pierde y que gana un analista cuando externaliza razonamiento en una vista visual?

---

## Laboratorio guiado de la semana

1. Instalar y abrir `Tableau`.
2. Cargar un `CSV` o `Excel`.
3. Identificar:
   - dimensiones
   - medidas
   - fechas
4. Crear:
   - una comparacion por categoria
   - una vista temporal o una dispersion
5. Guardar el workbook con convencion de nombres consistente.

---

## Criterios de calidad desde la semana 1

- Todo dashboard debe responder una **pregunta central**.
- Todo grafico debe tener una **razon de existencia**.
- Todo campo debe tener un **tipo correcto**.
- Todo hallazgo debe distinguir:
  - observacion
  - comparacion
  - interpretacion
  - accion sugerida

---

## Errores frecuentes

- Elegir la herramienta antes de definir la pregunta.
- Suponer que "interactivo" equivale a "mejor".
- Cargar datos sin revisar inferencia de tipos.
- Construir dashboards antes de conocer granularidad y calidad del dato.

---

## Actividad de cierre sugerida

1. Mostrar tres dashboards reales.
2. Pedir al grupo que identifique:
   - pregunta principal
   - publico objetivo
   - principal virtud
   - principal defecto
3. Cerrar con una matriz breve:
   - claridad
   - precision
   - accionabilidad
   - confiabilidad

---

## Bibliografia base

- Tamara Munzner, *Visualization Analysis and Design*
- Colin Ware, *Information Visualization*
- Stephen Few, *Show Me the Numbers*
- Cole Nussbaumer Knaflic, *Storytelling with Data*
