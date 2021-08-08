from Funciones import probabilidad_simple

class Calculadora:
    def __init__(self):
        pass

    def menu(self):
        print() #Crea un espacio en blanco
        menu= [
            ['Seleccione el calculo'],
            ['1. Probabilidad Simple'],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Salir'] 
            ]
        
        for x in range(6):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            self.probabilidad_simple()
            x=input("")
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo de la calculadora ...")
            exit()
        # Volvemos a llamar al menú
        self.menu()
        
    def probabilidad_simple(self):
        probabilidad_simple()
    




calculadora = Calculadora() 
calculadora.menu()