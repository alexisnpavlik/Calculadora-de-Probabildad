from Probabilidad import probabilidad_simple
import Estadistica

class Calculadora:
    def __init__(self):
        pass

    def menu(self):
        print() #Crea un espacio en blanco
        menu= [
            ['Seleccione el calculo'],
            ['1. Estadistica'],
            ['3. Medidas de tendencia central'],
            ['1. Probabilidad Simple'],
            ['5. Salir'] 
            ]
        
        for x in range(6):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
    
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            self.probabilidad_simple()
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo de la calculadora ...")
            exit()
        # Volvemos a llamar al menú
        self.menu()


calculadora = Calculadora() 
calculadora.menu()