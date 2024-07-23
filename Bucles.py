# Bucle For

# Sintaxis

# for i in range(11):
#     ......

# for i in range(1, 11, 1):
#     print(i)

# Reto 1
# Pedirle al usuario una palabra y imprimirla 5 veces

# text = str(input("Escribe algo: "))

# i = 0 
# for i in range(5): 
#     print(text) # 0, 1, 2, 3, 4
    
# Cuantas veces se imprime la palabra
# a) 1
# b) 2
# c) 4 //////
# d) 5 / ✅

# Reto 2cle
# Imprime 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# for i in range(1, 10 + 1): 
#     print(i)

# que se imprime
# a) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 /// ✅
# b) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
# c) 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 
# d) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /// 
# e) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# f) error
# g) nunguna de las anteriores /

# Reto 3
# Imprimir la suma de los números del 1 al 100:

# a = 0

# for i in range(1, 100 + 1): 
    
#     a = i + a 
#     print(a)

# Reto 4
# Imprimir los números pares del 1 al 20:

# for i in range(1, 20 + 1): 
#     if i % 2 == 0:
#         print(i)


# Reto 5
# Imprimir los números impares del 1 al 20:

# for i in range(1, 20 + 1): 
#     if i % 2 != 0:
#         print(i)

# Reto 6
# Imprimir la tabla de multiplicar del 7:

# for i in range(1, 10 + 1): 
#     print(f" 7 x {i} = {7 * i}")
    
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Reto 7
# Calcular el factorial de un número:

# num = int(input("Coloca el numero para allar el factorial: "))

# fact = 1

# for i in range(1, num + 1): 
    
#     fact *= i
#     print(fact)


# Reto 8
# Imprime los primeros 10 numeros de la serie fibonacci

# n = 10
# a = 0
# b = 1

# for i in range(n + 2):
#     print(a)
#     a, b = b, a + b
    

# Reto 9
# Crea un temporizador de 3 dijitos (h, m, s)

for i in range(10, -1, -1):
    for j in range(60, -1 , -1):
        for k in range(60, -1 , -1):
            for g in range(60, -1 , -1):
                print(f"{i},{j},{k},{g}")



##############################################################


