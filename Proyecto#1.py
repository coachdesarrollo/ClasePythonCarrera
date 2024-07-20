# 0. titulo: Tienda de postres ✅
# 1. Productos con precios ✅
# 2. preguntar al usuario el producto ✅
# 3. Preguntarle si quiere llevar otra cosa
# 4. preguntar si quiere finalizar la compra.

def menu(): # Funcion con el nombre menu
        # Menu con los precios
        try: # Colocamos el try para la exepcion de errores
            menu_pr = int(input(
            "\nBienvenido a Pinkie Pie!!!\n" "##########################\n"           "\n          Menu           \n\n" 
            "1. Pro1               $300\n"
            "2. Pro2               $500\n"
            "3. Pro3               $300\n" 
            "4. Pro4               $700\n" 
            "5. Pro5               $900\n" 
            "6. Pro6               $100\n" 
            "7. Pro7               $200\n"
            "8. Pro8               $700\n" 
            "9. Pro9               $500\n" 
            "10.Pro10              $400\n" 
            "Ingresa el numero del postre que desea comprar (Elija un solo producto): "))
        
            if menu_pr >= 1 and menu_pr <= 10:
                fin_compra = str(input("Desea terminar esta compra?(s/n): "))
            else:
                menu()
                
        except:
            menu()
       
        else:
            if (fin_compra == "s"):
                print("Compra realizada")
            else:
                menu()


        
menu()