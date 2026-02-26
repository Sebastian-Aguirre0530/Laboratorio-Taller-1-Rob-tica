import numpy as np
import matplotlib.pyplot as plt

def obtener_curva_pt100(r0, t_min, t_max, puntos=500):
    """
    Genera los datos de temperatura y resistencia usando 
    operaciones vectorizadas de Numpy.
    """
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12
    

    t = np.linspace(t_min, t_max, puntos)
    r = np.where(t >= 0,
                 r0 * (1 + A * t + B * t**2),
                 r0 * (1 + A * t + B * t**2 + C * (t - 100) * t**3))
    
    return t, r

def graficar_comportamiento(temp, res):
    """Maneja toda la lógica de visualización."""
    plt.figure(figsize=(10, 6))
    plt.plot(temp, res, color='teal', linewidth=2, label='Resistencia PT100')
    plt.axhline(100, color='red', linestyle='--', alpha=0.5, label='100 Ω a 0°C')
    plt.axvline(0, color='black', linewidth=1)
    
    plt.title('Curva de Calibración Sensor PT100', fontsize=14)
    plt.xlabel('Temperatura (°C)', fontsize=12)
    plt.ylabel('Resistencia (Ω)', fontsize=12)
    plt.grid(True, which='both', linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    t_data, r_data = obtener_curva_pt100(r0=100, t_min=-200, t_max=200)
    graficar_comportamiento(t_data, r_data)