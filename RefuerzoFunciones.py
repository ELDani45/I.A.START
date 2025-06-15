# # Ejericsio 1 - Función que calcule el área de un triángulo.

def calcular_area (base,altura):
    area = 0.5 * base * altura
    return area

print(calcular_area(8,5))

# # Ejercisio 2 - Función que determine si un número es par o impar.

def impar_o_par(numero):
    if numero % 2 == 0:
        return "el numero es par."
    else:
        return "el numero es impar."

print(impar_o_par(4))

# # Ejercisio 3 - Función que reciba una lista de números y devuelva el promedio.
def promedio(lista_notas):
    resultado = sum(lista_notas)/len(lista_notas)
    return round(resultado)


print(promedio(lista_notas = [3,5,7,3,5,6]))

# # Ejercisio 4 - Función que reciba nombre y edad, y diga si es mayor de edad o no.

def mayorDeEdad(edad):
    if edad <= 18:
        return "Eres mayor de edad."
    else:
        return "No eres mayor de edad."

print(mayorDeEdad(13))

# # Ejercisio 5 - Función que genere un saludo personalizado dependiendo de la hora (mañana, tarde, noche).

def saludo_personalizado(hora):
    if hora < 12:
        return "Buenos días"
    elif 12 <= hora < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"  

print(saludo_personalizado(10))
# # -------- REFURZO CON EJERCISIOS ALINEADOS A TENSORFLOW ---------

# Una IA toma decisiones basadas en números. Crea una función que simule un clasificador binario:
#  si el valor de entrada es mayor que un cierto umbral, devuelve "Positivo", si no, "Negativo".
# - La función debe llamarse clasificar(score, umbral=0.5).

def clasificar(score, umbral=0.5):
    if score > umbral:
        return f"Positivo (score={score} > umbral={umbral})"
    else:
        return f"Negativo (score={score} <= umbral={umbral})"

# # Resultado esperado:
print(clasificar(0.8))         # Positivo
print(clasificar(0.3))         # Negativo
print(clasificar(0.4, 0.2))    # Positivo

# EJERCISIO 2
# En IA es común normalizar los datos, es decir, convertirlos a una escala estándar.
# - Crea una función normalizar(lista) que reciba una lista de números y devuelva una nueva
# lista con los valores entre 0 y 1, usando esta fórmula:

def normalizar(lista):
    valorMIn = min(lista)
    valorMax = max(lista)
    rango = valorMax - valorMIn
    lista_Normalizada = []
    for x in lista:
        resultado = (x - valorMIn)/(rango)
        lista_Normalizada.append(resultado)
    return lista_Normalizada 
    
print(normalizar([2,4,7,8,9]))

# def normalizar(lista):
#     return [(x - min(lista))/ (max(lista)- min(lista)) for x in lista]


print(normalizar([2,5,7,8,9]))

# ---- EJERCISIOS SOBRE NORMALIZACION ----- #
# -  Ejercicio 1: Cuadrados normalizados
# Crea una función que reciba una lista de números, calcule su cuadrado, y luego los normalice entre 0 y 1.

def cuadrado(lista1):
    listacuadrado = []
    for x in lista1:
        r2 = x * x 
        normalizar = (r2 - min(lista1))/(max(lista1)-min(lista1))
        listacuadrado.append(normalizar)
    return listacuadrado

print(cuadrado([2,4,6,8,10]))

# Ejercisio 2 
#Crea una función que escale los valores de una lista para que estén entre -1 y 1.

def valor_escalado(lista3):
    lista_escalada = []
    rango = max(lista3)-min(lista3)
    for i in lista3:
        valorescalado = (2*(i-min(lista3)))/(rango)-1
        lista_escalada.append(valorescalado)
    return lista_escalada

print(valor_escalado([2,4,6]))
# EJERCISIO 3 
# Haz una función que reciba una lista, elimine los valores menores que 10, y normalice el resto.

def filtra(lista4):
    # Paso 1: eliminar los valores menores que 10
    filtrada = [x for x in lista4 if x >= 10]
    
    # Paso 2: calcular min, max y rango de la lista filtrada
    minimo = min(filtrada)
    maximo = max(filtrada)
    rango = maximo - minimo
    
    # Paso 3: normalizar la lista filtrada
    normalizada = [(x - minimo) / rango for x in filtrada]
    
    return normalizada

print(filtra([4, 8, 12, 16, 20])) 

# Resultado esperado: [0.0, 0.333, 0.666, 1.0]

# EJERCISIO 3 ALINEADOS CON TENSORFLOW. [CONTINUACION]

# 🔹 Ejercicio 4: Simulación de predicción de IA
# Simula una IA que predice un sentimiento a partir de una puntuación.

#  Crea una función predecir_sentimiento(puntaje) que devuelva:
# "Negativo" si puntaje < 0.4
# "Neutral" si está entre 0.4 y 0.6
# "Positivo" si > 0.6

def predecir_sentimiento(puntaje):
    if puntaje < 0.4:
        return "Negativo"
    elif 0.4 <= puntaje <= 0.6:
        return "Neutral"
    else:
        return "Positivo"

print(predecir_sentimiento(0.2))  # Negativo
print(predecir_sentimiento(0.5))  # Neutral
print(predecir_sentimiento(0.8))  # Positivo

# # # 🔹 Ejercicio 5: Calculadora de precisión
# # En aprendizaje automático se mide qué tan buena es una IA con métricas como la precisión.

# # 👉 Crea una función calcular_precision(aciertos, total) que devuelva la precisión como porcentaje redondeado a 2 decimales.

def calcular_precision(aciertos, total):
    precision = (aciertos / total) * 100
    return round(precision, 2)

print(calcular_precision(75, 100))  # 75.0
print(calcular_precision(18, 20))   # 90.0

# FORMULA = X * B + B

def neurona(x, w, b):
    resultado = (x * w) + b
    if resultado >= 0:
        return "Activo"
    else:
        return "Inactivo"
print(neurona(2, 0.5, -1))  # 1  →  (2 * 0.5) + (-1) = 0.0 → activo
print(neurona(1, -1, 0))    # 0  →  (1 * -1) + 0 = -1 → inactivo
print(neurona(0, 10, 1))    # 1  →  (0 * 10) + 1 = 1 → activo