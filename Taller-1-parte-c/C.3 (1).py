import numpy as np
import matplotlib.pyplot as plt

def calcular_curvas(V, R, C):
    """Calcula el tiempo y los voltajes de carga y descarga."""
    tau = R * C  
    t = np.linspace(0, 5 * tau, 1000)
    v_carga = V * (1 - np.exp(-t / tau))
    v_descarga = V * np.exp(-t / tau)
    
    return t, v_carga, v_descarga, tau

def generar_grafica(t, v_carga, v_descarga, V, tau):
    """Crea una comparativa visual de ambos procesos."""
    plt.figure(figsize=(10, 6))
    plt.plot(t, v_carga, label='Carga del Capacitor', color='teal', lw=2)
    plt.plot(t, v_descarga, label='Descarga del Capacitor', color='orangered', lw=2, linestyle='--')
    
    plt.axvline(x=tau, color='gray', linestyle=':', label=f'Tau (τ) = {tau:.4f}s')
    plt.title('Comportamiento de un Circuito RC', fontsize=14)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.ylim(-0.5, V + 0.5)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def main():
    print("--- Simulador de Carga/Descarga RC ---")
    try:

        v_fuente = float(input("Voltaje de la fuente (V): "))
        r_ohmios = float(input("Resistencia (Ω): "))
        c_microfaradios = float(input("Capacitancia (µF): "))
        
        c_faradios = c_microfaradios * 1e-6
        
        t, v_c, v_d, tau = calcular_curvas(v_fuente, r_ohmios, c_faradios)
        
        print(f"\n[INFO] Constante de tiempo (τ): {tau:.6f} segundos.")
        print(f"[INFO] El sistema se estabiliza aprox. a los {5*tau:.6f} segundos.")
        
        generar_grafica(t, v_c, v_d, v_fuente, tau)
        
    except ValueError:
        print("Error: Por favor, ingresa valores numéricos.")

if __name__ == "__main__":
    main()