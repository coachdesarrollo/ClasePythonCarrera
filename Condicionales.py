
# Condicionales

# 1. Condicional Simple
# 2. Condicional Doble
# 3. Condicional Anidado
# 4. Condicional Multiple


# Si la condicion se cumple nos ejecuta lo que esta dentro del bloque de codigo

# 1. Condicional Simple

# if (4 > 5): 
#     print("")

# Reto 6

# Pide un numero si el numero colocado en mayor a 5 imprimir en pantalla

# num = float(input("Coloca un numero: "))

# if (1 > 2):
#     print("numero 1 es el mayor")


# print("numero 1 no es el mayor")
    
# ¿Que pasa si ejecuto el codigo?
# a. Se imprimen los dos
# b. se imprime solo el de la condicion /
# c. Se imprime solo el de afuera /////

# if (2 > 1):
#     print("numero 1 es el mayor")


# print("numero 1 no es el mayor")

# ¿Que pasa si ejecuto el codigo?
# a. Se imprimen los dos //////
# b. se imprime solo el de la condicion 
# c. Se imprime solo el de afuera 

##################################

# Condicional Doble

# if ():
#     print("")
# else:
#     print("")

############################


# if (2 > 1):
#     print("numero 1 es el mayor")
# else: # Default // Por Defecto
#     print("numero 1 no es el mayor")

# ¿Que pasa si ejecuto el codigo?

# a. Se imprimen los dos 
# b. se imprime solo el de arriba /
# c. Se imprime solo el de abajo

# if (1 > 2):
#     print("numero 1 es el mayor")
# else: # Default // Por Defecto // Solo se ejecuta si la condicion no de cumple.
#     print("numero 1 no es el mayor")

# ¿Que pasa si ejecuto el codigo?

# a. Se imprimen los dos 
# b. se imprime solo el de arriba
# c. Se imprime solo el de abajo /

#######################################

# Reto 7
# Pedir la edad y si es mayor o igual a 18 imprimir es mayor de edad si no imprimir es menor de edad

# Reto 8
# Determinar si es Mayor de Edad

# edad = int(input("Cuantos años tienes: "))

# if (edad >= 18):
#     print("Eres mayor de edad")
# else: 
#     print("Eres menor de edad")


# ¿Que pasa si pongo un numero decimal?

# a. Explota el codigo //////
# b. El codigo funciona normal
# c. Tira else

#########################################

# Reto 9
# Verificación de Contraseña

# Esta variable me permite verificar la contraseña.
# <nombre de la variable> = "<contraseña>"

# verificado = "aegis"
# contraseña = str(input("Ingrese su contraseña: "))

# if (verificado == contraseña):
#     print("Su contraseña es correcta")
# else:
#     print("Error: Su contraseña es incorrecta ")


##################################################

# Reto 10
# División con Verificación de Cero con dos numeros // Evita que se pueda dividir entre 0

# 5 / 0 = Error
# 0 / 5 = 0

#######################

# Esta variable almacena numeros
# num1 = float(input("ingrese el primer numero: "))
# num2 = float(input("ingrese el segundo numero: "))

# Que pasa si coloco un numero entero
# a. Explota el codigo 
# b. El codigo convierte el numero en decimal //////
# c. El codigo es feo

##############

# print(5 / 0)

# Que pasa si imprimo esta operacion
# a. Se explota ////
# b. da 0 /
# c. da 5
# d. da infinito /

###############

# print(0 / 5)

# Que pasa si imprimo esta operacion
# a. Se explota /
# b. da 0 
# c. da 5
# d. da infinito

##############################3


# num1 = 4
# num2 = 0


# if num1 == 0 and num2 == 0:
#     print("No se puede dividir entre 0")
# else:
#     print(f"Su resultado es: {num1 / num2} y su residuo es: {num2 % num1}")


# Que se ejecuta en este caso:

# Este caso da error: Porque esta dividiendo entre 0 y no sirve el codigo por que esta feo.

########################

# num1 = float(input("ingrese el primer numero: ")) # Dividendo 
# num2 = float(input("ingrese el segundo numero: ")) # Divisor

# if num2 == 0:
#     print("No se puede dividir entre 0")
# else:
#     print(f"Su resultado es: {num1 / num2} y su residuo es: {num1 % num2}")


################################################

# Reto 11
# Determinar si un Número es Par o Impar

# num = float(input("Ingresa un numero: "))

# if (num % 2 == 0):
#     print("Su numero es par")
# else:
#     print("Su numero es impar")



################################################

# Reto 12
# Determinar Si Debe Tributar

# Todas las personas naturales que cumplan con alguna de las siguientes condiciones deben declarar el impuesto sobre la renta 2024:
# Que el patrimonio bruto al término del año gravable 2023 sea igual o superior a $190.854.000.
# Que los ingresos totales del respectivo ejercicio gravable sean iguales o superiores a $59.377.000.

# patrimonio = float(input("ingresa tu patrimonio del año pasado sin comas ni puntos: "))

# # ingresos totales
# ing_total = float(input("ingresa tus ingresos totales del año pasado: "))

# if patrimonio >= 190854000 and ing_total >= 59377000:
#     print("Estas jodido debes declarar renta, yaper, llorindeli")
# else:
#     print("Aleluya, que suerte tienes no tienes que hacer nada aun estas pobre")



################################################

# Retos Para los Estudiantes

# Reto 13
# Asignación a Grupos

# (\n) Sirve para bajarnos el texto una linea

# select_group = str(input("a que grupo deseas ingresar: \n Grupo A \n Grupo B \n Grupo C \n ingresa la letra del grupo: "))

# ¿Que pasa si coloco un numero?
# a.implociona
# b. El codigo funciona normal
# c. El numero se vuelve un String /////


# if (select_group == "a" or select_group == "A" or select_group == "a." or select_group == "A."):
#     print("Esta en el grupo A")
# elif (select_group == "b" or select_group == "B" or select_group == "b." or select_group == "B."):
#     print("Esta en el grupo B")
# elif (select_group == "c" or select_group == "C" or select_group == "c." or select_group == "C."):
#     print("Esta en el grupo C")
# else:
#     print("Colocaste la letra que no era")

# Reto 14
# Calcular Tipo Impositivo
# ct_tributaria = float(input("Ingresa la cuota tributaria: "))
# ig_imponible = float(input("Ingresa la cuota tributaria: "))

# res = (ct_tributaria / ig_imponible) * 100


# # Maneras de concatenar 
# print("Tu impositivo es: ", res)
# print("Tu impositivo es: %s " %res)
# print(f"Tu impositivo es: {res} ")
# print("Tu impositivo es: {} ".format(res))



# Reto 15
# Evaluación de Desempeño (3 bajo desempeño)(4 mediano desempeño)(alto desempeño)

# Reto 16
# Precio de Entrada según Edad (18 años // puede entrar // menos de 18 años // no puede entrar)

# Reto 17
# Selección de Pizza // se creativo


##############################################

# Condicional Anidado

# Estructura

# if ():
#     if ():
# else:


##----------------


# Ejemplo 1:

# if (5<6):
#     print("5 si es menor que 6")
#     if (5<9):
#         print("5 si es menor que 9")
#     else:
#         print("5 es mayor que 3")
# else:
#     print("5 es el numero menor")


# Reto 18

# Pide dos numeros, busca cual es el mayor y ordenalos.

###------------------------------

# Estructura

# if ():
#     if ():
# else:
#     if ():


# Ejemplo 2

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# if (num1 > num2):
#     # valor 1
#     print("numero 1 es el mayor")
# else:
#     if (num1 < num2):
#         # valor 2
#         print("numero 2 es el mayor")
#     else:
#         # valor 3
#         print("Los dos numeros son iguales")

# Reto 19

# Escribe un codigo que arroje exactamente los mismos valores del ejemplo 2 sin cambiar nada pero que tenga una sintaxis distinta al ejemplo 2..

###-----------------------------------------------------

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# if (num1 > num2):
#     # valor 1
#     print("numero 1 es el mayor")

# elif (num1 < num2):
#         # valor 2
#         print("numero 2 es el mayor")
# elif (num1 == num2):
#         # valor 3
#         print("Los dos numeros son iguales")
# else:
#    print("no le sabes ")

###----------------------------------------------------

# num1 = float(input("Ingresa el primer numero: "))
# num2 = float(input("Ingresa el segundo numero: "))

# if (num1 > num2):
#     # valor 1
#     print("numero 1 es el mayor")
# elif (num1 < num2):
#         # valor 2
#         print("numero 2 es el mayor")
# else:
#    print("Los dos numeros son iguales")

###----------------------------------------------------

# num1, num2 = float(input("Ingresa el primer numero: ")), float(input("Ingresa el segundo numero: "))

# n1_mayor_n2, n2_mayor_n1, n2_equal_n1 = num1 > num2, num1 < num2, num1 == num2

# if n1_mayor_n2:
#     # valor 1
#     print("numero 1 es el mayor")
# elif n2_mayor_n1:
#         # valor 2
#         print("numero 2 es el mayor")
# elif n2_equal_n1:
#         # valor 3
#         print("Los dos numeros son iguales")

##---- ACTIVIDAD DE REPASO ----##

# num = float(input("Coloca un numero numerico: "))

# if num == 0:
#     print("El numero es 0")
# elif (num % 2 == 0):
#     print("El numero es par")
# else:
#     print("El numero es impar")

# num = float(input("Coloca un numero numerico: ")) ## 0

# if (num % 2 == 0):
#      print("El numero es par")
# elif num == 0:
#     print("El numero es 0")
   

# Si la variable num almacena un 0 que arroja

# a. el numero es par 
# b. eñ numero es 0 


### ----- Estrucuta de control -----###

# if condición:
     # código a ejecutar si la condición es verdadera
# elif otra_condición:
     # código a ejecutar si la otra condición es verdadera
# else:
    # código a ejecutar si ninguna condición anterior es verdadera


#################################################################

# Reto 20: Calcular el índice de masa corporal (IMC) y clasificarlo.

## Operacion // Peso entre altura elevado a la dos

## 18.5 Peso Bajo
## 18.6 a 24.9 Peso normal
## 25 a 29.9 Sobrepeso
## 30 para arriba obesidad


#######################################################

# Reto 21: Calificación escolar
# Escribe un programa que pida al usuario una calificación (número entre 0 y 100) y determine la letra correspondiente a esa calificación según la escala siguiente:

# A[ª] (90-100)
# B (80-89)
# C (70-79)
# D (60-69)
# F (0-59)

# hallar el numero mayor de 3 numeros


# Condicional Multiple



