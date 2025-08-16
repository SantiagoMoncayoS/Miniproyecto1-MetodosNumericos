
---

# 📄 `punto2/README.md`

```markdown
# Punto 2 – Estabilidad y orden

Este punto estudia el problema de **decaimiento exponencial** y compara tres métodos numéricos: Forward Euler, Backward Euler y Crank–Nicolson.

---

## 📂 Contenido

- `app/run_stability.py` → Script principal con los experimentos de estabilidad y orden.  
- `numerics/methods.py` → Clases para cada método numérico (`ForwardEuler`, `BackwardEuler`, `CrankNicolson`).  
- `numerics/errors.py` → Rutina para calcular el error global en norma L2.

---

## ▶️ Ejecución

Desde la raíz del repositorio:

```bash
python -m punto2.app.run_stability
```

El script realiza:

1. Simulación del problema u' = -λ u con diferentes pasos de tiempo.
2. Cálculo del error global y estimación del orden de convergencia.
3. Gráficos:
  -Error global vs paso de tiempo (log–log).
  -Regiones de estabilidad a partir del factor de amplificación.
  -Evolución temporal de cada método en distintos regímenes.

Resultados esperados:
  -Forward Euler: orden ≈ 1, estable solo si λΔt ≤ 2.
  -Backward Euler: orden ≈ 1, A-estable.
  -Crank–Nicolson: orden ≈ 2, A-estable.
