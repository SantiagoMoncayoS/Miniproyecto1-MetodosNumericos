# -*- coding: utf-8 -*-
import numpy as np

def exact_solution(t, lam=1.0, u0=1.0):
    return u0 * np.exp(-lam * t)

def l2_error(u_num, t, lam=1.0, u0=1.0):
    """Aproxima la norma L2 del error ~ sqrt(dt * sum (e_n)^2)."""
    u_ex = exact_solution(t, lam, u0)
    dt = t[1] - t[0]
    e = u_num - u_ex
    return float(np.sqrt(dt * np.sum(e * e)))
