# Ejercicio Básico de Números:

# def describe_number(num):
#     match num:
#         case 0:
#             return "Cero"
#         case 1:
#             return "Uno"
#         case 2:
#             return "Dos"
#         case _:
#             return "Otro número"

# print(describe_number(1))  # Uno
# print(describe_number(5))  # Otro número
# Días de la Semana:


# def day_of_week(day):
#     match day:
#         case 1:
#             return "Lunes"
#         case 2:
#             return "Martes"
#         case 3:
#             return "Miércoles"
#         case 4:
#             return "Jueves"
#         case 5:
#             return "Viernes"
#         case 6:
#             return "Sábado"
#         case 7:
#             return "Domingo"
#         case _:
#             return "Día no válido"

# print(day_of_week(3))  # Miércoles
# Colores del Semáforo:

# def traffic_light(color):
#     match color:
#         case "rojo":
#             return "Detente"
#         case "amarillo":
#             return "Prepárate"
#         case "verde":
#             return "Avanza"
#         case _:
#             return "Color no válido"

# print(traffic_light("verde"))  # Avanza
# Tipos de Datos:

# data = 13

# data = type(data)

# print(data)

# match data:
#     case "int":
#         print( "Entero")
#     case float():
#         print( "Decimal")
#     case str():
#         print("Cadena")
#     case bool():
#         print("Booleano")
#     case _:
#         print("Otro tipo de dato")

# Decimal
# Operaciones Matemáticas Simples:

# python
# Copy code
# def simple_calculator(a, b, operation):
#     match operation:
#         case "suma":
#             return a + b
#         case "resta":
#             return a - b
#         case "multiplicación":
#             return a * b
#         case "división":
#             return a / b if b != 0 else "División por cero"
#         case _:
#             return "Operación no válida"

# print(simple_calculator(10, 5, "suma"))  # 15
# Estaciones del Año:

# python
# Copy code
# def season(month):
#     match month:
#         case 12 | 1 | 2:
#             return "Invierno"
#         case 3 | 4 | 5:
#             return "Primavera"
#         case 6 | 7 | 8:
#             return "Verano"
#         case 9 | 10 | 11:
#             return "Otoño"
#         case _:
#             return "Mes no válido"

# print(season(4))  # Primavera
# Clasificación de Edad:

# python
# Copy code
# def age_group(age):
#     match age:
#         case age if age < 13:
#             return "Niño"
#         case age if 13 <= age < 18:
#             return "Adolescente"
#         case age if 18 <= age < 65:
#             return "Adulto"
#         case age if age >= 65:
#             return "Anciano"
#         case _:
#             return "Edad no válida"

# print(age_group(25))  # Adulto
# Identificación de Forma Geométrica:

# python
# Copy code
# def shape(sides):
#     match sides:
#         case 3:
#             return "Triángulo"
#         case 4:
#             return "Cuadrado o Rectángulo"
#         case 5:
#             return "Pentágono"
#         case 6:
#             return "Hexágono"
#         case _:
#             return "Otra forma"

# print(shape(4))  # Cuadrado o Rectángulo