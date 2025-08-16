import numpy as np

def trapz(fy: np.ndarray, x: np.ndarray) -> float:
    return np.trapz(fy, x)

def simpson(fy: np.ndarray, x: np.ndarray) -> float:
    try:
        from scipy.integrate import simpson as sp_simpson
        return float(sp_simpson(fy, x))
    except Exception:
        N = len(x)
        if N % 2 == 0:
            x = x[:-1]; fy = fy[:-1]; N -= 1
        h = (x[-1] - x[0]) / (N - 1)
        S = fy[0] + fy[-1] + 4 * fy[1:-1:2].sum() + 2 * fy[2:-1:2].sum()
        return float(S * h / 3.0)
