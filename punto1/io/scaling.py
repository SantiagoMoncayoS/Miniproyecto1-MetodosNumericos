import numpy as np
from punto1.models.profile import ProfileData

class ImageScaler:
    """Convierte puntos en pixeles a (y, r) en cm usando el diametro de la boca."""
    def __init__(self, mouth_diameter_cm: float):
        self.R_boca = mouth_diameter_cm / 2.0

    def pixels_to_profile(self, pts_xy: np.ndarray) -> ProfileData:
        x_pix, y_pix = pts_xy[:,0], pts_xy[:,1]
        x_min = np.min(x_pix)
        r_pix = x_pix - x_min
        r_pix_boca = np.max(r_pix)
        if r_pix_boca <= 0:
            raise ValueError("No se detecto radio en pixeles valido.")
        scale = self.R_boca / r_pix_boca

        r_cm = r_pix * scale
        y_pix_base = np.max(y_pix)
        y_cm = (y_pix_base - y_pix) * scale

        data = ProfileData(y_cm=y_cm, r_cm=r_cm)
        data.validate()
        return data
