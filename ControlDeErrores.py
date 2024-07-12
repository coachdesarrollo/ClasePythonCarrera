# Excepciones // Sintaxis
# try: // Ingresa todo el codigo que queremos poner en cuarentena
# except:
# else:
# finally:

try:
    num = int(input("Coloca un numero: ")) # 3
    num2 = int(input("Coloca otro numero: ")) # 3.4
    
except:
    print("Coloca un numero correcto: ")
else: 
    print(num + num2)
finally:
    print("Esta es la respuesta: ")
 
    