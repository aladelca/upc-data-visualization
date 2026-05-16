import type { HeightMetric, LayerMode, VisualizationState } from "./types";

type ControlHandlers = {
  onChange: (state: VisualizationState) => void;
  onFit: () => void;
};

type Controls = {
  layerMode: HTMLSelectElement;
  heightMetric: HTMLSelectElement;
  verticalScale: HTMLInputElement;
  themeToggle: HTMLButtonElement;
  fitMap: HTMLButtonElement;
  status: HTMLElement;
};

function getElement<T extends HTMLElement>(id: string, type: { new (): T }): T {
  const element = document.getElementById(id);
  if (!(element instanceof type)) {
    throw new Error(`Missing expected element #${id}`);
  }
  return element;
}

export function readControls(): Controls {
  return {
    layerMode: getElement("layer-mode", HTMLSelectElement),
    heightMetric: getElement("height-metric", HTMLSelectElement),
    verticalScale: getElement("vertical-scale", HTMLInputElement),
    themeToggle: getElement("theme-toggle", HTMLButtonElement),
    fitMap: getElement("fit-map", HTMLButtonElement),
    status: getElement("data-status", HTMLElement),
  };
}

export function bindControls(
  controls: Controls,
  initialState: VisualizationState,
  handlers: ControlHandlers,
): void {
  let state = initialState;

  const publish = (partial: Partial<VisualizationState>) => {
    state = {...state, ...partial};
    controls.themeToggle.textContent = state.theme === "light" ? "Modo oscuro" : "Modo claro";
    handlers.onChange(state);
  };

  controls.layerMode.addEventListener("change", () => {
    publish({layerMode: controls.layerMode.value as LayerMode});
  });

  controls.heightMetric.addEventListener("change", () => {
    publish({heightMetric: controls.heightMetric.value as HeightMetric});
  });

  controls.verticalScale.addEventListener("input", () => {
    publish({verticalScale: Number.parseFloat(controls.verticalScale.value)});
  });

  controls.themeToggle.addEventListener("click", () => {
    publish({theme: state.theme === "light" ? "dark" : "light"});
  });

  controls.fitMap.addEventListener("click", handlers.onFit);
}

export function setStatus(element: HTMLElement, message: string, isWarning = false): void {
  element.textContent = message;
  element.classList.toggle("status-warning", isWarning);
}
