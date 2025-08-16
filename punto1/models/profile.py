from dataclasses import dataclass
import numpy as np

@dataclass
class ProfileData:
    """Perfil axial de la chocolatera como (y, r) en cm, ordenados por y ascendente."""
    y_cm: np.ndarray
    r_cm: np.ndarray

    def validate(self):
        assert self.y_cm.ndim == 1 and self.r_cm.ndim == 1
        assert self.y_cm.size == self.r_cm.size >= 4, "Se requieren >= 4 puntos."
        # asegurar orden
        idx = np.argsort(self.y_cm)
        self.y_cm = self.y_cm[idx]
        self.r_cm = self.r_cm[idx]


