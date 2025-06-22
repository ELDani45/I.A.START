# MATRIZES

import numpy as np

# Tresdimensiones = np.array([[[10, 20, 30],[21, 34, 67]],[[10, 20, 30],[21, 34, 67]]])
# print("Mi array con NumPy:", Tresdimensiones)
# print(Tresdimensiones.ndim)

# dosDimensiones = np.array([[1, 4, 5, 7, 8],[12, 23, 45, 17,22]])
# print(dosDimensiones.ndim)

# # Mostra el numero de filas y colimnas ".shape"
# matriz = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print("forma:",matriz.shape) # Forma: (3,3) porque tiene 3 filas y 3 columnas.

# # c. Toda la fila 1 (segunda fila):
# print("Fila 1:", matriz[1])

# # d. Toda la columna 2 (tercera columna):

# print("Columna 2:", matriz[:, 2])

# # e. El elemento en la fila 0, columna 1:
# print("Elemento [0,1]:", matriz[0, 1])

# print("Elemento: ", matriz[0])

# Crea una función llamada clasificar_multiplo(numero) que:

# Devuelva "Múltiplo de 2 y 5" si el número es múltiplo de ambos

# Devuelva "Solo múltiplo de 2" si es múltiplo de 2 pero no de 5

# Devuelva "Solo múltiplo de 5" si es múltiplo de 5 pero no de 2

# Devuelva "No es múltiplo de 2 ni de 5" si no es múltiplo de ninguno

# def clasificar_multiplo(numero):
#     if numero % 2 == 0 and numero % 5 == 0:
#         return "Múltiplo de 2 y 5"
#     elif numero % 2 == 0:
#         return "Solo múltiplo de 2"
#     elif numero % 5 == 0:
#         return "Solo múltiplo de 5"
#     else:
#         return "No es múltiplo de 2 ni de 5"


# print(clasificar_multiplo(10))  # Múltiplo de 2 y 5
# print(clasificar_multiplo(4))   # Solo múltiplo de 2
# print(clasificar_multiplo(25))  # Solo múltiplo de 5
# print(clasificar_multiplo(7))   # No es múltiplo de 2 ni de 5

# Promedio 
matrizPromedio = np.array([[1,3,4,6,8],[10,13,14,16,29]])

print(np.mean(matrizPromedio[0,1:4]))
# suma 
print(np.sum(matrizPromedio[1]))

# Iteracion 

for filas in matrizPromedio:
    print(filas)