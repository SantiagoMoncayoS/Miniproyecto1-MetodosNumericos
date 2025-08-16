import os
import numpy as np
import matplotlib

# Fuerza un backend interactivo. TkAgg suele estar disponible en Windows.
try:
    matplotlib.use("TkAgg")
except Exception:
    pass  # si falla, matplotlib elegira el disponible

import matplotlib.pyplot as plt

class ImageDigitizer:
    """Permite recolectar puntos del borde derecho en la imagen."""
    def __init__(self, image_path: str):
        self.image_path = image_path

    def collect_points(self) -> np.ndarray:
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"No se encontro la imagen: {self.image_path}")

        img = plt.imread(self.image_path)

        fig, ax = plt.subplots(figsize=(5, 7))
        ax.imshow(img)
        ax.set_axis_off()

        try:
            fig.canvas.manager.set_window_title(
                "Selecciona puntos: click izquierdo; cierra la ventana al terminar"
            )
        except Exception:
            pass

        # Asegura que la ventana aparezca
        plt.show(block=False)

        # Ahora si: ginput espera clicks en la figura activa
        print("Haz click en el borde derecho (base -> boca). Cierra la ventana cuando termines.")
        pts = plt.ginput(n=-1, timeout=0)  # clicks ilimitados; cerrar ventana para terminar
        plt.close(fig)

        pts = np.array(pts, dtype=float)
        if pts.shape[0] < 4:
            raise ValueError("Se requieren >= 4 puntos para el ajuste.")
        return pts
