# Miniproyecto 1 – Métodos Numéricos para Ecuaciones en Derivadas Parciales

Repositorio de entrega del **Miniproyecto 1** para la materia *Métodos Numéricos para Ecuaciones en Derivadas Parciales* (2025-2).  
Profesor: **José Hernán Ortiz Ocampo**

---

## 📂 Contenido del repositorio

- `punto1/` → Código fuente del **Punto 1 (La chocolatera)**  
  - `app/main.py` → Script principal para ejecutar la solución.  
  - `io/`, `models/`, `numerics/` → módulos y clases auxiliares (digitización de puntos, escalado, curvas, integración numérica, cálculo de volumen).  
  - `chocolatera.png` → Imagen utilizada como referencia.  

- `punto2/` → Código fuente del **Punto 2 (Estabilidad y orden en el problema de decaimiento exponencial)**  
  - `app/run_stability.py` → Script principal con experimentos de error y estabilidad.  
  - `numerics/methods.py` → Métodos implementados como clases (`ForwardEuler`, `BackwardEuler`, `CrankNicolson`).  
  - `numerics/errors.py` → Rutinas para cálculo de error L2.  

- `punto3/` → Documentación y archivos en LaTeX del **Punto 3 (Cambio de variables y jacobiano)**  
  - `punto3.tex` → Documento en LaTeX con la explicación.  
  - `punto3.pdf` → Compilación en PDF.  
  - `docs/punto3.md` → Explicación en Markdown.  

- `docs/` → Documentación en Markdown de cada punto:  
  - `docs/punto1.md` → Documentación del Punto 1.  
  - `docs/punto2.md` → Documentación del Punto 2.  
  - `docs/punto3.md` → Documentación del Punto 3.  

- `requirements.txt` → Dependencias necesarias para recrear el ambiente virtual.  

---

## ⚙️ Configuración del ambiente virtual

Se recomienda usar **Python 3.10 o superior**.  
Pasos para reproducir el entorno:

```bash
# 1. Crear y activar un ambiente virtual
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt
