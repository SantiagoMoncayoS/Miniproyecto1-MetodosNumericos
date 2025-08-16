# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from ..numerics.methods import ForwardEuler, BackwardEuler, CrankNicolson
from ..numerics.errors import l2_error

def estimate_slope(xs, ys, idx_lo=1, idx_hi=-1):
    """Pendiente de log10(y) vs log10(x) en un rango 'interior' para evitar extremos ruidosos."""
    lx = np.log10(xs[idx_lo:idx_hi])
    ly = np.log10(ys[idx_lo:idx_hi])
    m, b = np.polyfit(lx, ly, 1)
    return float(m), float(b)

def run_order_experiment(lam=1.0, u0=1.0, T=1.0):
    dts = np.logspace(-4, -1, 10)   # 1e-4 ... 1e-1

    methods = [
        ("Forward Euler", ForwardEuler()),
        ("Backward Euler", BackwardEuler()),
        ("Crank–Nicolson", CrankNicolson()),
    ]

    all_errs = {}

    for name, method in methods:
        errs = []
        for dt in dts:
            t, u = method.solve(lam, u0, dt, T)
            errs.append(l2_error(u, t, lam, u0))
        all_errs[name] = np.array(errs)

    # Estimar órdenes (pendientes)
    for name in all_errs:
        m, _ = estimate_slope(dts, all_errs[name], idx_lo=2, idx_hi=-2)
        print(f"{name:>16}  ~ orden ≈ {m:.2f}")

    # Gráfico log-log
    plt.figure(figsize=(6,4))
    for name, style in zip(all_errs.keys(), ["o-", "s-", "^-"]):
        plt.loglog(dts, all_errs[name], style, label=name)
    plt.gca().invert_xaxis()
    plt.xlabel(r"$\Delta t$")
    plt.ylabel("Error L2")
    plt.title("Error global vs paso de tiempo")
    plt.legend()
    plt.tight_layout()
    plt.show()

def run_stability_experiment():
    """Verifica estabilidad viendo |G(a)| y trayectorias largas."""
    methods = [
        ("Forward Euler", ForwardEuler()),
        ("Backward Euler", BackwardEuler()),
        ("Crank–Nicolson", CrankNicolson()),
    ]

    a_vals = np.linspace(0, 4, 200)  # a = lambda*dt
    plt.figure(figsize=(6,4))
    for name, method in methods:
        G = np.array([abs(method.amplification(a)) for a in a_vals])
        plt.plot(a_vals, G, label=name)
    plt.axhline(1.0, color="k", linestyle="--", linewidth=1)
    plt.xlabel(r"$a=\lambda\,\Delta t$")
    plt.ylabel(r"$|G(a)|$")
    plt.title("Factor de amplificación |G(a)|")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Trayectorias para dt grandes/pequeños (u'=-lam u debería decaer)
    lam, u0, T = 1.0, 1.0, 10.0
    tests = [
        ("FE estable (a=1.0)", ForwardEuler(), 1.0/lam),   # dentro de [0,2]
        ("FE inestable (a=3.0)", ForwardEuler(), 3.0/lam), # fuera del rango
        ("BE (a=5.0)", BackwardEuler(), 5.0/lam),          # estable
        ("CN (a=5.0)", CrankNicolson(), 5.0/lam),          # estable
    ]
    plt.figure(figsize=(6,4))
    for label, method, dt in tests:
        t, u = method.solve(lam, u0, dt, T)
        plt.plot(t, u, label=label)
    plt.xlabel("t"); plt.ylabel("u(t)")
    plt.title("Comportamiento temporal (estabilidad)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 1) Orden de convergencia (pendiente log-log)
    run_order_experiment(lam=1.0, u0=1.0, T=1.0)

    # 2) Estabilidad (|G|<=1 y trayectorias)
    run_stability_experiment()
