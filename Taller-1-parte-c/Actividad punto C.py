import numpy as np
import matplotlib.pyplot as plt

# ==================== FUNCIONES INDIVIDUALES ====================
def dibujar_A(x, y):
    plt.plot([x, x+1], [y, y+3], 'b-', linewidth=2)
    plt.plot([x+1, x+2], [y+3, y], 'b-', linewidth=2)
    plt.plot([x+0.5, x+1.5], [y+1.5, y+1.5], 'b-', linewidth=2)

def dibujar_B(x, y):
     plt.plot([x, x], [y, y+3], 'b-', linewidth=2)        
     plt.plot([x, x+0.5], [y, y], 'b-', linewidth=2) 
     plt.plot([x, x+1.15], [y+3, y+3], 'b-', linewidth=2)  
     plt.plot([x, x+1.15], [y, y], 'b-', linewidth=2)       
     plt.plot([x, x+1.2], [y+1.5, y+1.5], 'b-', linewidth=2) 
     t = np.linspace(-np.pi/2, np.pi/2, 20)
     plt.plot(x + 1.2 + 0.3*np.cos(t), y + 2.25 + 0.75*np.sin(t), 'b-', linewidth=2) 
     plt.plot(x + 1.2 + 0.3*np.cos(t), y + 0.75 + 0.75*np.sin(t), 'b-', linewidth=2)

    

def dibujar_E(x, y):
    plt.plot([x, x], [y, y+3], 'b-', linewidth=2)
    plt.plot([x, x+2], [y+3, y+3], 'b-', linewidth=2)
    plt.plot([x, x+1.5], [y+1.5, y+1.5], 'b-', linewidth=2)
    plt.plot([x, x+2], [y, y], 'b-', linewidth=2)

def dibujar_H(x, y):
    plt.plot([x, x], [y, y+3], 'b-', linewidth=2)
    plt.plot([x+2, x+2], [y, y+3], 'b-', linewidth=2)
    plt.plot([x, x+2], [y+1.5, y+1.5], 'b-', linewidth=2)

def dibujar_I(x, y):
    plt.plot([x+1, x+1], [y, y+3], 'b-', linewidth=2)

def dibujar_J(x, y):
    plt.plot([x, x+2], [y+3, y+3], 'b-', linewidth=2)
    plt.plot([x+2, x+2], [y+3, y], 'b-', linewidth=2)
    plt.plot([x+2, x], [y, y], 'b-', linewidth=2)
    plt.plot([x, x], [y, y+0.8], 'b-', linewidth=2)


def dibujar_N(x, y):
    plt.plot([x, x], [y, y+3], 'b-', linewidth=2)
    plt.plot([x+2, x+2], [y, y+3], 'b-', linewidth=2)
    plt.plot([x, x+2], [y+3, y], 'b-', linewidth=2)

def dibujar_O(x, y):
   plt.plot([x, x+2], [y, y], 'b-', linewidth=2)  
   plt.plot([x, x+2], [y+3, y+3], 'b-', linewidth=2)  
   plt.plot([x, x], [y, y+3], 'b-', linewidth=2) 
   plt.plot([x+2, x+2], [y, y+3], 'b-', linewidth=2) 

def dibujar_R(x, y):
    plt.plot([x, x], [y, y+3], 'b-', linewidth=2)
    plt.plot([x, x+1.5], [y+3, y+3], 'b-', linewidth=2)
    plt.plot([x+1.5, x+1.5], [y+1.5, y+3], 'b-', linewidth=2)
    plt.plot([x, x+1.5], [y+1.5, y+1.5], 'b-', linewidth=2)
    plt.plot([x, x+2], [y+1.5, y], 'b-', linewidth=2)

def dibujar_S(x, y):
    plt.plot([x, x+2], [y+3, y+3], 'b-', linewidth=2)
    plt.plot([x, x], [y+1.5, y+3], 'b-', linewidth=2)
    plt.plot([x, x+2], [y+1.5, y+1.5], 'b-', linewidth=2)
    plt.plot([x+2, x+2], [y, y+1.5], 'b-', linewidth=2)
    plt.plot([x, x+2], [y, y], 'b-', linewidth=2)


def dibujar_T(x, y):
    plt.plot([x, x+2], [y+3, y+3], 'b-', linewidth=2)
    plt.plot([x+1, x+1], [y, y+3], 'b-', linewidth=2)

def dibujar_V(x, y):
    plt.plot([x, x+1], [y+3, y], 'b-', linewidth=2)
    plt.plot([x+1, x+2], [y, y+3], 'b-', linewidth=2)

# ==================== LOGOS ====================
def chevrolet(x, y):
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot(x + 1.5*np.cos(t), y + 1.5*np.sin(t), 'r-', linewidth=2)
    plt.plot([x-1, x+1], [y, y], 'r-', linewidth=3)
    plt.plot([x, x], [y-1, y+1], 'r-', linewidth=3)
    plt.text(x, y-2, "Chevrolet", ha='center')

def hyundai(x, y):
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot(x + 2*np.cos(t), y + 1.2*np.sin(t), 'b-', linewidth=2)
    plt.plot([x-0.8, x-0.8], [y-1.0, y+1.0], 'b-', linewidth=3)
    plt.plot([x+0.8, x+0.8], [y-1.0, y+1.0], 'b-', linewidth=3)
    plt.plot([x-0.8, x+0.8], [y-1.0, y+1.0], 'b-', linewidth=3)
    plt.text(x, y-2, "Hyundai", ha='center')


   

# ==================== DICCIONARIO ====================
letras = {
    'A': dibujar_A, 'B': dibujar_B, 'E': dibujar_E, 'H': dibujar_H,
    'I': dibujar_I, 'J': dibujar_J, 'N': dibujar_N, 'O': dibujar_O,
    'R': dibujar_R, 'S': dibujar_S, 'T': dibujar_T, 'V': dibujar_V
}

# ==================== FIGURA 1: NOMBRES ====================
plt.figure(1, figsize=(20, 10))

# EVAN
x = 2
y = 15.5
dibujar_E(x, y)
dibujar_V(x+3, y)
dibujar_A(x+6, y)
dibujar_N(x+9, y)
plt.text(x, y+3.8, "EVAN", fontsize=14, fontweight='bold', color='darkblue')

# SEBASTIAN
x = 2
y = 10.5
dibujar_S(x, y)
dibujar_E(x+3, y)
dibujar_B(x+6, y)
dibujar_A(x+9, y)
dibujar_S(x+12, y)
dibujar_T(x+15, y)
dibujar_I(x+18, y)
dibujar_A(x+21, y)
dibujar_N(x+24, y)
plt.text(x, y+3.8, "SEBASTIAN", fontsize=14, fontweight='bold', color='darkblue')

# HARRISON
x = 2
y = 5.5
dibujar_H(x, y)
dibujar_A(x+3, y)
dibujar_R(x+6, y)
dibujar_R(x+9, y)
dibujar_I(x+12, y)
dibujar_S(x+15, y)
dibujar_O(x+18, y)
dibujar_N(x+21, y)
plt.text(x, y+3.8, "HARRISON", fontsize=14, fontweight='bold', color='darkblue')

# JAHIR
x = 2
y = 0.5
dibujar_J(x, y)
dibujar_A(x+3, y)
dibujar_H(x+6, y)
dibujar_I(x+9, y)
dibujar_R(x+12, y)
plt.text(x, y+3.8, "JAHIR", fontsize=14, fontweight='bold', color='darkblue')

# Ajustes de la Figura 1
plt.gca().set_aspect('equal')
plt.xlim(0, 35)
plt.ylim(0, 20)
plt.grid(True, alpha=0.3, linestyle='--')
plt.title("NOMBRES DEL GRUPO", fontsize=18, fontweight='bold', color='navy')
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)

# ==================== FIGURA 2: LOGOS ====================
plt.figure(2, figsize=(12, 8))

# LOGOS
plt.text(15, 16, "LOGOS DE AUTOMÓVILES", fontsize=16, fontweight='bold', color='darkred', ha='center')
chevrolet(15, 12)
hyundai(15, 7)
mazda(15, 2)

# Ajustes de la Figura 2
plt.gca().set_aspect('equal')
plt.xlim(5, 25)
plt.ylim(0, 18)
plt.grid(True, alpha=0.3, linestyle='--')
plt.title("LOGOS DE AUTOMÓVILES", fontsize=18, fontweight='bold', color='darkred')
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)

# Mostrar ambas figuras
plt.show()
    
    
    
   
   








            
    