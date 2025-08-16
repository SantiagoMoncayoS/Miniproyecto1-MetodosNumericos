from abc import ABC, abstractmethod
import numpy as np

try:
    from scipy.interpolate import splrep, splev
    _SCIPY_OK = True
except Exception:
    _SCIPY_OK = False

class BaseCurve(ABC):
    @abstractmethod
    def eval(self, y: np.ndarray) -> np.ndarray:
        ...

class SplineCurve(BaseCurve):
    """Spline cubica r(y). Requiere SciPy."""
    def __init__(self, y_cm: np.ndarray, r_cm: np.ndarray, smooth: float = 0.0):
        if not _SCIPY_OK:
            raise RuntimeError("SciPy no disponible: use PolyCurve.")
        self._tck = splrep(y_cm, r_cm, s=smooth, k=3)

    def eval(self, y: np.ndarray) -> np.ndarray:
        from scipy.interpolate import splev
        r = splev(y, self._tck)
        return np.clip(r, 0.0, None)

class PolyCurve(BaseCurve):
    """Polinomio r(y) de grado dado (sin SciPy)."""
    def __init__(self, y_cm: np.ndarray, r_cm: np.ndarray, deg: int = 4):
        self._coef = np.polyfit(y_cm, r_cm, deg)

    def eval(self, y: np.ndarray) -> np.ndarray:
        r = np.polyval(self._coef, y)
        return np.clip(r, 0.0, None)
