import numpy as np
import matplotlib.pyplot as plt

def plot_profile(y_cm: np.ndarray, r_cm: np.ndarray, y_fit: np.ndarray, r_fit: np.ndarray):
    plt.figure(figsize=(5,4))
    plt.plot(y_cm, r_cm, 'o', label='Datos (cm)')
    plt.plot(y_fit, r_fit, '-', label='Ajuste')
    plt.xlabel('y [cm]'); plt.ylabel('r [cm]')
    plt.title('Perfil r(y)')
    plt.legend(); plt.tight_layout(); plt.show()
