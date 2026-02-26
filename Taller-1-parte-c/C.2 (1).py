import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def clasificar_sistema(a, b, c):
    """Calcula el discriminante y clasifica el sistema."""
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Subamortiguado", "royalblue"
    elif delta == 0:
        return "Críticamente amortiguado", "forestgreen"
    else:
        return "Sobreamortiguado", "crimson"

def graficar_respuesta(a, b, c, tipo, color):
    """Genera la respuesta al escalón usando NumPy para el tiempo."""
    sistema = signal.TransferFunction([1], [a, b, c])
    t = np.linspace(0, 20, 1000) 
    t, y = signal.step(sistema, T=t)
    
    plt.figure(figsize=(9, 5))
    plt.plot(t, y, color=color, lw=2, label=f'Tipo: {tipo}')
    plt.axhline(y=1/c, color='gray', linestyle='--', label='Valor final (Estado estable)')  
    plt.title('Respuesta Temporal del Sistema', fontsize=12)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

def main():
    print("--- Analizador de Sistemas de 2do Orden ---")
    try:
        a = float(input("Coeficiente a (s^2): "))
        b = float(input("Coeficiente b (s): "))
        c = float(input("Coeficiente c (cte): "))
        
        tipo, color = clasificar_sistema(a, b, c)
        print(f"\n>>> Sistema Detectado: {tipo.upper()}")
        
        graficar_respuesta(a, b, c, tipo, color)
        
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()