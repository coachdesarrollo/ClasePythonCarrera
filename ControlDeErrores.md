
# 1. División por cero.
# 2. Conversión de cadena a número.
# 3. Acceso a un índice fuera de rango en una lista.
# 4. Apertura de un archivo inexistente.
# 5. Uso de un método en una variable con tipo incorrecto.
# 6. División por un valor no numérico.
# 7. Conversión de cadena a flotante.
# 8. Acceso a una clave inexistente en un diccionario.
# 9. Manejo de múltiples excepciones.
# 10. Entrada de usuario con validación de tipo.


# #######################################################

División por cero:

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    else:
        return resultado

print(dividir(10, 2))
print(dividir(10, 0))

# #######################################################

Conversión de cadena a número:

def convertir_a_entero(cadena):
    try:
        numero = int(cadena)
    except ValueError:
        return "No se puede convertir a entero"
    else:
        return numero

print(convertir_a_entero("123"))
print(convertir_a_entero("abc"))

# #######################################################

<!-- Acceso a un índice fuera de rango en una lista:


lista = [1, 2, 3]

try:
    print(lista[5])
except IndexError:
    print("Índice fuera de rango") -->

# #######################################################

<!-- Apertura de un archivo inexistente:

try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("El archivo no existe") -->

# #######################################################

<!-- Uso de un método en una variable con tipo incorrecto:


numero = 10

try:
    numero.append(5)
except AttributeError:
    print("El objeto no tiene el método 'append'") -->

# #######################################################

División por un valor no numérico:


def dividir(a, b):
    try:
        resultado = a / b
    except TypeError:
        return "Los valores deben ser numéricos"
    else:
        return resultado

print(dividir(10, 2))
print(dividir(10, "a"))

# #######################################################

Conversión de cadena a flotante:


def convertir_a_flotante(cadena):
    try:
        numero = float(cadena)
    except ValueError:
        return "No se puede convertir a flotante"
    else:
        return numero

print(convertir_a_flotante("123.45"))
print(convertir_a_flotante("abc"))

# #######################################################

<!-- Acceso a una clave inexistente en un diccionario:

diccionario = {"clave1": "valor1"}

try:
    print(diccionario["clave2"])
except KeyError:
    print("La clave no existe en el diccionario") -->

# #######################################################

Manejo de múltiples excepciones:

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except TypeError:
        return "Los valores deben ser numéricos"
    else:
        return resultado

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))

# #######################################################

Entrada de usuario con validación de tipo:

def pedir_entero():
    try:
        numero = int(input("Introduce un número entero: "))
    except ValueError:
        print("La entrada no es un número entero")
    else:
        print(f"Has introducido el número entero: {numero}")

pedir_entero()