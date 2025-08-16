# Punto 1 – La chocolatera

Este punto consiste en modelar la forma de una chocolatera como un sólido de revolución y calcular su volumen mediante integración numérica.

---

## 📂 Contenido

- `app/main.py` → Script principal que ejecuta el flujo completo.  
- `io/` → Recolección de puntos en la imagen y escalado px→cm.  
- `models/` → Clase `ProfileData` para almacenar los datos del perfil.  
- `numerics/` → Curvas ajustadas (spline/polinomio), integración (trapecio y Simpson) y cálculo de volumen.  
- `chocolatera.png` → Imagen de referencia usada para digitalizar el perfil.

---

## ▶️ Ejecución

Desde la raíz del repositorio:

```bash
python -m punto1.app.main
```
Pasos al ejecutar:

1. Se abre la imagen de la chocolatera.
2. Haz clic en el borde derecho desde la base hasta la boca (≥4 puntos).
3. Cierra la ventana para continuar.
4. El programa ajusta el perfil, calcula el volumen con los métodos de Trapecio y Simpson, y muestra los errores relativos respecto al valor experimental (2200 ml).
5. Se genera un gráfico con el perfil digitizado y la curva ajustada.
