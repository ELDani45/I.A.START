# Ejericsio 1 - Función que calcule el área de un triángulo.

def calcular_area (base,altura):
    area = 0.5 * base * altura
    return area

print(calcular_area(8,5))

# Ejercisio 2 - Función que determine si un número es par o impar.

def impar_o_par(numero):
    if numero % 2 == 0:
        return "el numero es par."
    else:
        return "el numero es impar."

print(impar_o_par(4))

# Ejercisio 3 - Función que reciba una lista de números y devuelva el promedio.
def promedio(lista_notas):
    resultado = sum(lista_notas)/len(lista_notas)
    return round(resultado)


print(promedio(lista_notas = [3,5,7,3,5,6]))

# Ejercisio 4 - Función que reciba nombre y edad, y diga si es mayor de edad o no.

def mayorDeEdad(edad):
    if edad <= 18:
        return "Eres mayor de edad."
    else:
        return "No eres mayor de edad."

print(mayorDeEdad(13))

# Ejercisio 5 - Función que genere un saludo personalizado dependiendo de la hora (mañana, tarde, noche).

def saludo_personalizado(hora):
    if hora < 12:
        return "Buenos días"
    elif 12 <= hora < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"  

print(saludo_personalizado(10))