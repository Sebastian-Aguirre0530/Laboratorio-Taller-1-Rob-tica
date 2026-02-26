import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def graficar_vector_3d(x, y, z):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, x, y, z, color='crimson', lw=3, arrow_length_ratio=0.1)

    max_val = np.max([np.abs(x), np.abs(y), np.abs(z), 1])
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title(f'Vector v = ({x}, {y}, {z})')
    
    plt.show()

def main():
    print("--- Visualizador de Vectores en 3D ---")
    try:
        x_user = float(input("Ingrese X: "))
        y_user = float(input("Ingrese Y: "))
        z_user = float(input("Ingrese Z: "))
        graficar_vector_3d(x_user, y_user, z_user)
    except ValueError:
        print("Error: Ingrese solo números.")

if __name__ == "__main__":
    main()