# Bucle For

# Sintaxis

# for i in range(11):
#     .......

# for i in range(1, 11, 1):
#     print(i)

# Reto 1
# Pedirle al usuario una palabra y imprimirla 5 veces

# text = str(input("Escribe algo: "))

# for i in range(5):
#     print(text)

# Reto 2
# Imprime 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Reto 3
# Imprimir la suma de los números del 1 al 100:

# Reto 4
# Imprimir los números pares del 1 al 20:

# Reto 5
# Imprimir los números impares del 1 al 20:

# Reto 6
# Imprimir la tabla de multiplicar del 7:

# Reto 7
# Calcular el factorial de un número:

# num = int(input("Coloca el numero para allar el factorial: "))

# fact = 1

# for i in range(1, num + 1):
#     fact -= i
#     print(fact)


# Contador 

# for i in range(5, 2, -1):
#     for j in range(4, 1, -1):
#         print(f"{i}.{j}")

##############################################################


n = 10
a = 0
b = 1

for i in range(n + 2):
    print(a)
    a, b = b, a + b