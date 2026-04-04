# Semana 13: Ingenieria de dashboards, interactividad y publicacion

## Slide 1. Proposito de la semana

- Integrar vistas en un dashboard navegable, consistente y performante.
- Diseñar interaccion con intencion analitica.
- Preparar un producto listo para publicar o presentar.

---

## Slide 2. Fundamento teorico

- Un dashboard es una arquitectura de lectura, no una coleccion de graficos.
- La buena interaccion reduce esfuerzo y aumenta capacidad de exploracion controlada.
- Tres principios rectores:
  - foco
  - navegabilidad
  - rendimiento

---

## Slide 3. Arquitectura del dashboard final

![Dashboard engineering](./assets/dashboard-engineering.svg)

- Vista principal:
  - responde la pregunta central
- Vista de contexto:
  - permite comparar, explicar o segmentar
- Detail on demand:
  - da profundidad solo cuando el usuario la necesita

---

## Slide 4. Interactividad con criterio

- Filter actions:
  - para cambiar universo de observacion
- Highlight actions:
  - para seguir correspondencias sin perder contexto
- Parameter actions:
  - para escenarios o switches de metrica
- Viz in tooltip:
  - para detalle puntual sin saturar el layout principal

---

## Slide 5. Rendimiento y publicacion

- Reducir numero de hojas innecesarias.
- Evitar filtros redundantes.
- Controlar granularidad.
- Revisar calculos costosos.
- Publicar en Tableau Public o empaquetar workbook.
- Si se compara con Power BI, hacerlo en terminos de:
  - modelado
  - narrativa
  - integracion
  - publicacion

---

## Slide 6. Laboratorio guiado

1. Ensamblar dashboard final.
2. Agregar una accion interactiva bien justificada.
3. Validar:
   - comprension inicial
   - consistencia visual
   - tiempo de carga
4. Publicar o dejar listo para publicacion.

---

## Slide 7. Errores frecuentes

- Interactividad por exhibicion, no por necesidad.
- Demasiados filtros visibles.
- Vista principal sin pregunta dominante.
- Dashboards lentos por exceso de hojas y calculos.
- Publicar sin revisar sensibilidad de los datos.

---

## Slide 8. Referencias

- Stephen Few, *Information Dashboard Design*
- Kirk, *Data Visualisation*
- Tableau Public, buenas practicas de publicacion

