import numpy as np
from punto1.numerics.integrators import trapz, simpson

class VolumeCalculator:
    """Calcula V = pi * int r(y)^2 dy para un solido de revolucion."""
    def __init__(self, curve, y_min: float, y_max: float, npts: int = 1000):
        self.curve = curve
        self.y_grid = np.linspace(y_min, y_max, npts)

    def volume_trapz(self) -> float:
        r = self.curve.eval(self.y_grid)
        return float(np.pi * trapz(r**2, self.y_grid))

    def volume_simpson(self) -> float:
        r = self.curve.eval(self.y_grid)
        return float(np.pi * simpson(r**2, self.y_grid))

    @staticmethod
    def rel_error(v_num: float, v_exp: float) -> float:
        return abs(v_num - v_exp) / v_exp
