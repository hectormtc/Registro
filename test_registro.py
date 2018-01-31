import random

lista_Clientes = []

global numero

def Menu_1():
    print("""
            BIENVENIDO AL SISTEMA DE REGISTRO

            Opciones:

            1) Crear nuevo cliente
            0) Salir
            """)

def Menu_2():
    print("""
            SISTEMA DE REGISTRO

            Opciones:

            1) Crear nuevo cliente
            2) Buscar Clientes
            0) Salir
            """)

Menu_1()

opcion = int(input("    Opcion: "))


class Cliente(object):

    def __init__(self):

        self.idt = input("Id: ")
        self.nombre = input("Nombre: ")
        self.sexo = input("Mujer/Varon: ")
        self.edad = input("Edad: ")
        self.telefono = input("Telefono: ")

    def imprimir_Datos(self):

        print("ID: " + self.idt +
              '{}'.format("."))
        print("Nombre: " + self.nombre +
              '{}'.format("."))
        print("Sexo: " + self.sexo +
              '{}'.format("."))
        print("Edad: " + self.edad +
              '{}'.format("años"))
        print("Telefono:" + self.telefono +
              '{}'.format("."))

    def generador_Id():
        return random.randint(1000, 9000)

    def crear():
        numero = 0
        numero = numero - 1
        numero += 1

        print("\nID Generado: ", Cliente.generador_Id(), "\n")
        nuevo_cliente = "cliente_" + str(numero)
        print("ID del Cliente: ", nuevo_cliente)
        nuevo_cliente = Cliente()
        lista_Clientes.append(nuevo_cliente)
        print("¡Cliente agregado satisfactoriamente!\n")


    def buscar():

        buscar = int(input("Ingrese su id: cliente_"))

        try:
            if lista_Clientes[buscar] == False:
                print("ID no encontrada\n")
            else:
                print("\nID encontrada\n")
                lista_Clientes[buscar].imprimir_Datos()
        except:
            pass


while opcion != 0:

    if opcion == 1:
        print(Cliente.crear())
        print(Menu_2())

    elif opcion == 2:
        print (Cliente.buscar())
        print(Menu_2())

    elif opcion == 0:
        exit()

    else:
        try:
            print ("Ingrese una opcion correcta\n")
        except:
            pass

    opcion = int(input("    Opcion: "))