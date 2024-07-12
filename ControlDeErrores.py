# Excepciones // Sintaxis
# try: // Ingresa todo el codigo que queremos poner en cuarentena
# except: // agarra el error y ejecuta el codigo que nosotros coloquemos
# else: // Solo se ejecuta cuando no hay una Excepciones
# finally: // Siempre se ejecuta

try:
    num = int(input("Coloca un numero: ")) # 3
    num2 = int(input("Coloca otro numero: ")) # 3.4
    
except:
    print("no colocaste un numero correcto")
    
else: 
    print(num + num2)

 
    