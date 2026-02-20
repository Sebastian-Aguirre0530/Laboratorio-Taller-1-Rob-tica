import numpy as np
import math

###PUNTO 1 DEL TALLER 1
         #Operaciones
def operaciones_del_vector():
    vector1 = np.array([3 , 4, 7])
    vector2 = np.array([9, 1, 3])
    suma = vector1 + vector2
    resta = vector1 - vector2
    division = vector1 / vector2
    producto_punto = np.dot(vector1, vector2)
    producto_cruz = np.cross(vector1, vector2)
     
     #Resultados dados por los vectores 
    print("Vectores:")
    print(f"vector 1 = {vector1}")
    print(f"vector 2 = {vector2}")
    print(f"Suma de los vectores es: {suma}")
    print(f"Resta de los vectores es: {resta}")
    print(f"División del vector 1 y el vector 2 son: {division}")
    print(f" Resultado del producto punto es: {producto_punto}")
    print(f"Resultado del producto cruz es: {producto_cruz}")
    


#### PUNTO 2 DEL TALLER 1
def operacion_del_matriz():
    matriz1 = np.array([[6, 2], [5, 9]])
    matriz2 = np.array([[5, 6], [7, 8]])
    suma = matriz1 + matriz2
    resta = matriz1 - matriz2
    division = matriz1 / matriz2
    prod_punto = np.dot(matriz1, matriz2)
    prod_elemento = matriz1 * matriz2
    
    print("Matrices:")
    print(f"Matriz 1 = {matriz1}")
    print(f"Matriz 2 = {matriz2}")
    print(f"Suma de las matrices es = {suma}")
    print(f"Resta de las matrices es = {resta}")
    print(f"División de las matrices es =\n{division}")
    print(f"El producto punto de la matriz es:\n{prod_punto}")
    print(f"El producto elemento es:\n{prod_elemento}")

### Punto 3 del taller 1
#Valor de las variables 
X= 3
Y= 4.55
Z= 1

def conversion_de_coordenadas_CR_a_CCI_y_CE(X,Y,Z):
    distancia_del_radio_CCI= math.sqrt(X**2 + Y**2)
    Angulo_CCI= math.atan2(Y,X)
    Angulo_grados_CCI= math.degrees(Angulo_CCI)

    distancia_del_radio_CR_a_CE= math.sqrt(X**2 + Y**2 + Z**2)
    Angulo_CR_a_CE= math.atan2(Y,X)
    Angulo_grados_CR_a_CE= math.degrees(Angulo_CR_a_CE)
    
    if distancia_del_radio_CR_a_CE > 0:
       Angulo_polar= math.acos(Z / distancia_del_radio_CR_a_CE)
    else:
         Angulo_polar= 0.0
    ###conversion del angulo polar a grados
    Angulo_polar_grados= math.degrees(Angulo_polar)

    print(f"Coordenadas de inicio : X={X}, Y={Y}, Z={Z}")
    print(f"Distancia del radio Coordenadas Cilindricas: {distancia_del_radio_CCI:,.3f},cm")
    print(f"Ángulo en radianes de la coodernadas rectangulares a cilindricas: {Angulo_CCI:,.2f},rad")
    print(f"Angulo en grados de las coordenadas  rectangulares a cilindricas: {Angulo_grados_CCI:,.2f}°")
    print(f"Distancia del radio Coordenadas rectangulares a esfericas: {distancia_del_radio_CR_a_CE:,.2f},mm")
    print(f"Ángulo en radianes de las coordenadas rectangulares a esfericas: {Angulo_CR_a_CE:,.2f},rad")
    print(f"Ángulo en grados de las coordenadas rectangulares a esfericas: {Angulo_grados_CR_a_CE:,.2f}°")
    print(f"Ángulo polar en radianes: {Angulo_polar:,.2f},rad")
    print(f"Ángulo polar en grados: {Angulo_polar_grados:,.2f}°")

### Punto 4 del taller 1
def Calculo_de_la_PT100():
    temperatura = [77] #en grados Celsius
    Valor_Resitencia_inicial= 100.0 #Cuando la temperatura es de 0°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  # Para temperaturas < 0°C
    
    for temp in temperatura:
        if temp >= 0:
            resistencia = Valor_Resitencia_inicial * (1 + A * temp + B * temp**2)
        else:
            resistencia = Valor_Resitencia_inicial * (1 + A * temp + B * temp**2 + C * (temp - 100) * temp**3)

    print(f"Resistencia del PT100: {resistencia:.2f} ohms")




#### Punto 5 del taller 1
def Rotaciones_en_los_ejes():
    Angulo_inicial= 65 #dado en grados
    Angulo_radianes= math.radians(Angulo_inicial) #Convertir el ángulo a radianes, funciona para las funciones trigonométricas en Python
    Coseno_del_angulo= math.cos(Angulo_radianes)
    Seno_del_angulo= math.sin(Angulo_radianes)

    Rotacion_en_Z= np.array([
        [Coseno_del_angulo, -Seno_del_angulo, 0],
        [Seno_del_angulo, Coseno_del_angulo, 0],
        [0, 0, 1]
    ])

    Rotacion_en_X= np.array([
        [1,0,0],
        [0, Coseno_del_angulo, -Seno_del_angulo],
        [0, Seno_del_angulo, Coseno_del_angulo], 
    ])

    Rotacion_en_Y= np.array([
        [Coseno_del_angulo, 0, Seno_del_angulo],
        [0, 1, 0],
        [-Seno_del_angulo, 0, Coseno_del_angulo],
    ])  

    print(f"Ángulo inicial en grados es: {Angulo_inicial}°")
    print(f"Ángulo convertido a radianes es: {Angulo_radianes:.2f} radianes")
    print(f"Coseno del ángulo dado es: {Coseno_del_angulo:.3f}°")
    print(f"Seno del ángulo dado es: {Seno_del_angulo:.3f}°")
    print(f"Matriz de rotación en el eje Z:\n{Rotacion_en_Z}")
    print(f"Matriz de rotación en el eje X:\n{Rotacion_en_X}")
    print(f"Matriz de rotación en el eje Y:\n{Rotacion_en_Y}")

matriz_z, matriz_x, matriz_y = Rotaciones_en_los_ejes()

print("\n--- Matrices fueron3 retornadas ---")
print(f"Matriz Z retornada:\n{matriz_z}")
print(f"Matriz X retornada:\n{matriz_x}")
print(f"Matriz Y retornada:\n{matriz_y}")


#### Punto 6 del taller 1
diametro_del_embolo= 30 #en milimetros
diametro_del_vastago= 98 #en milimetros
presion_del_cilindro= 6.2 
eficiencia_del_cilindro= 0.85
longitud_de_la_carrera= 500 #en milimetros

def fuerza_de_avance_y_retroceso_del_cilindro():
    area_del_embolo= math.pi * (diametro_del_embolo / 2) ** 2
    area_del_vastago= math.pi * (diametro_del_vastago / 2) ** 2
    fuerza_de_avance= presion_del_cilindro * area_del_embolo * eficiencia_del_cilindro
    fuerza_de_retroceso= presion_del_cilindro * (area_del_embolo - area_del_vastago) * eficiencia_del_cilindro

    print(f"Área del émbolo: {area_del_embolo:.2f} mm²")
    print(f"Área del vástago: {area_del_vastago:.2f} mm²")
    print(f"Fuerza de avance del cilindro: {fuerza_de_avance:.2f} N")
    print(f"Fuerza de retroceso del cilindro: {fuerza_de_retroceso:.2f} N")



### RESULTADOS DE LOS PUNTOS 1 - 6 DEL TALLER 1
if __name__ == "__main__":
   operaciones_del_vector()

   operacion_del_matriz()

   conversion_de_coordenadas_CR_a_CCI_y_CE(X,Y,Z)

   Calculo_de_la_PT100()

   Rotaciones_en_los_ejes()

   fuerza_de_avance_y_retroceso_del_cilindro()
