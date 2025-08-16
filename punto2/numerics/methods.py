from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

class TimeStepper(ABC):
    """Interfaz para metodos de un paso: u_{n+1} = G(a) u_n, a = lambda*dt."""
    @abstractmethod
    def amplification(self, a: float) -> float:
        """Factor de amplificacion G(a)."""
        ...

    def solve(self, lam: float, u0: float, dt: float, T: float):
        """Integra u' = -lam*u desde 0 hasta T con paso dt."""
        N = int(np.round(T / dt))
        t = np.linspace(0.0, N * dt, N + 1)
        u = np.zeros_like(t)
        u[0] = u0
        a = lam * dt
        G = self.amplification(a)
        for n in range(N):
            u[n + 1] = G * u[n]
        return t, u

class ForwardEuler(TimeStepper):
    """u_{n+1} = (1 - a) u_n, estable si |1 - a| <= 1  => 0 <= a <= 2."""
    def amplification(self, a: float) -> float:
        return 1.0 - a

class BackwardEuler(TimeStepper):
    """u_{n+1} = u_n / (1 + a), A-estable (|G|<1 para a>0)."""
    def amplification(self, a: float) -> float:
        return 1.0 / (1.0 + a)

class CrankNicolson(TimeStepper):
    """u_{n+1} = ((1 - a/2)/(1 + a/2)) u_n, A-estable y orden 2."""
    def amplification(self, a: float) -> float:
        return (1.0 - 0.5 * a) / (1.0 + 0.5 * a)
