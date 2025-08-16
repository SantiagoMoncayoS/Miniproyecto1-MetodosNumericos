import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # agrega '.../punto1' al sys.path

from punto1.io.image_points import ImageDigitizer
from punto1.io.scaling import ImageScaler
from punto1.io.plotter import plot_profile
from punto1.numerics.curve import SplineCurve, PolyCurve
from punto1.numerics.volume import VolumeCalculator

 #Ruta robusta: desde app/main.py sube a carpeta punto1 y toma chocolatera.png
BASE_DIR = Path(__file__).resolve().parents[1]  
IMG_PATH = BASE_DIR / "chocolatera.png"          
DIAM_BOCA_CM = 12.3
V_EXP_ML = 2200.0
USE_SPLINE = True
POLY_DEG = 4

def main():
    digit = ImageDigitizer(str(IMG_PATH))
    pts = digit.collect_points()

    scaler = ImageScaler(mouth_diameter_cm=DIAM_BOCA_CM)
    prof = scaler.pixels_to_profile(pts)

    if USE_SPLINE:
        curve = SplineCurve(prof.y_cm, prof.r_cm, smooth=0.0)
    else:
        curve = PolyCurve(prof.y_cm, prof.r_cm, deg=POLY_DEG)

    y_min, y_max = float(prof.y_cm.min()), float(prof.y_cm.max())
    vc = VolumeCalculator(curve, y_min, y_max, npts=1201)
    v_trap = vc.volume_trapz()
    v_simp = vc.volume_simpson()
    e_trap = vc.rel_error(v_trap, V_EXP_ML)
    e_simp = vc.rel_error(v_simp, V_EXP_ML)

    print(f"Altura estimada: {prof.y_cm.max():.2f} cm")
    print(f"Volumen Trapecio: {v_trap:.1f} ml | Error rel: {100*e_trap:.2f}%")
    print(f"Volumen Simpson : {v_simp:.1f} ml | Error rel: {100*e_simp:.2f}%")

    y_fit = np.linspace(y_min, y_max, 800)
    r_fit = curve.eval(y_fit)
    plot_profile(prof.y_cm, prof.r_cm, y_fit, r_fit)

if __name__ == "__main__":
    main()

