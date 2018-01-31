#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

lista_Clientes = [] #Los clientes se guardaran en listas por su respectivo numero
numero = 0 #Guarda la suma de cantidad de clientes

def Menu():
    print("\t" + "-" * 42)

    print("""
        SISTEMA DE REGISTRO

        Opciones:

        1) Crear nuevo cliente
        2) Buscar Clientes
        3) Modificar registro
        4) Cantidad de Clientes
        0) Salir
    """)
    print("\t" + "-" * 42)

Menu()
opcion = int(input("\t\tOpcion: ")) #Pide la opcion para poder continuar con el programa


class Cliente(object):
    def __init__(self): #Se inicia pidiendo los datos

        self.contra = input("\tContraseña: ")
        self.nombre = input("\tNombre: ")
        self.sexo = input("\tMujer/Hombre: ")
        self.edad = input("\tEdad: ")
        self.telefono = input("\tTelefono: ")

        validacion = input("\n\t¿Crear registro registro(S/n)?: ")

        while validacion != "S":

            if validacion == "n":
                print("\n\tContraseña Generada: ", Cliente.generador_Contra(), "\n")

                self.contra = input("\tContraseña: ")
                self.nombre = input("\tNombre: ")
                self.sexo = input("\tMujer/Hombre: ")
                self.edad = input("\tEdad: ")
                self.telefono = input("\tTelefono: ")

                validacion = input("\n\t¿Crear registro(S/n)?: ")
            else:
                print ("\n\tSolo "'S'" o "'n'" ")
                validacion = input("\n\t¿Crear registro(S/n)?: ")

    def establecer_Modificacion(self):

        print("\n\tContraseña Generada: ", Cliente.generador_Contra(), "\n")

        self.contra = input("\tContraseña: ")
        self.nombre = input("\tNombre: ")
        self.sexo = input("\tMujer/Hombre: ")
        self.edad = input("\tEdad: ")
        self.telefono = input("\tTelefono: ")

        modificacion = input("\n\t¿Modificar registro(S/n)?: ")

        while modificacion != "n":

            if modificacion == "S":
                print("\n\tContraseña Generada: ", Cliente.generador_Contra(), "\n")

                self.contra = input("\tContraseña: ")
                self.nombre = input("\tNombre: ")
                self.sexo = input("\tMujer/Hombre: ")
                self.edad = input("\tEdad: ")
                self.telefono = input("\tTelefono: ")

                modificacion = input("\n\t¿Modificar registro(S/n)?: ")
            else:

                print("\n\tSolo "'S'" o "'n'"\n")

            modificacion = input("\n\t¿Modificar registro(S/n)?: ")

    def imprimir_Datos(self): #Imprime los datos una vez guardados

        print("\tContraseña: " + self.contra + '{}'.format("."))
        print("\tNombre: " + self.nombre + '{}'.format("."))
        print("\tSexo: " + self.sexo + '{}'.format("."))
        print("\tEdad: " + self.edad + '{}'.format(" años"))
        print("\tTelefono: " + self.telefono + '{}'.format("."))

    def modificar_Registro():

        buscar_modificacion = int(input("\n\tIngrese su id: cliente_"))

        try:

            if lista_Clientes[buscar_modificacion] != False: #Busca si el cliente se encuentra en la lsita

                print("\n\tNombre: " + lista_Clientes[buscar_modificacion].nombre + '{}'.format("."))

                pregunta_Modificar = input("\n\t¿Desea modificar este registro?(S/n): ")

                while pregunta_Modificar != "n":

                    if pregunta_Modificar == "S":

                        lista_Clientes[buscar_modificacion].establecer_Modificacion()
                        print("\n\t¡Cliente Modificado Satisfactoriamente!\n")

                    else:

                        print("\n\tSolo S o n")
                    pregunta_Modificar = input("\n\t¿Desea modificar este registro?(S/n): ")
            else:

                pass
        except:

            print ("\n\t¡Cliente no encontrado!\n")

    def generador_Contra():#Genera una contraseña random entre 1000 y 9000

        return random.randint(1000, 9000)

    def crear():

        print("\n\tContraseña Generada: ", Cliente.generador_Contra(), "\n") #Llama a la funcion generador_Id()

        nuevo_cliente = Cliente() #Se crea la variable nuevo_cliente para heredar la clase Cliente()
        lista_Clientes.append(nuevo_cliente) #Se agrega esa nueva variable a la lista, lista_Clientes

        print("\n\t¡Cliente agregado satisfactoriamente!\n")

    def buscar():

        buscar = int(input("\n\tIngrese su id: cliente_"))#El id del cliente es el numero que dio al incio "cliente_"

        try:
            if lista_Clientes[buscar] == False:

                pass
            else:

                print("\n\tID encontrada\n")
                lista_Clientes[buscar].imprimir_Datos()#Imprime los datos del cliente
        except:

            print("\n\tID no encontrada\n")

    def cantidad_Clientes():

        print ("\n\tCantidad de clientes: ", len(lista_Clientes), "\n")

        Menu()

########################################################################################################################

while opcion != 0:

    if opcion == 1:

        print("\t"+"-"*40)

        numero += 1 #Cuando se crea un nuevo cliente, se suma 1 para indicar el id del cliente nuevo.
        nuevo_cliente = "cliente_" + str(int(numero-1))#Se crea la variable que va a mostrar el nuevo cliente
        print("\n\tID del Cliente: "+nuevo_cliente)#Imprime el id del nuevo cliente
        Cliente.crear()#Llama a la funcion de crear un nuevo cliente para ser guardado en la lista.

        Menu()
    elif opcion == 2:

        if len(lista_Clientes[:]) == 0:

            print("\n\tNo hay Clientes aun\n")
            Menu()
        else:
            pass

        while len(lista_Clientes[:]) > 0:

            print("\t" + "-"*40)
            Cliente.buscar()#Busca al cliente
            Menu()

            break

    elif opcion == 3:

        if len(lista_Clientes[:]) == 0:

            print("\n\tNo hay Clientes aun\n")

        else:
            pass

        while len(lista_Clientes[:]) > 0:

            print("\t" + "-"*40)
            opcion_modificar = input("\n\t¿Desea modificar un registro?(S/n): ")

            while opcion_modificar != "n":

                if opcion_modificar == "S":

                    Cliente.modificar_Registro()

                else:
                    print ("\n\tSolo S o n")
                opcion_modificar = input("\n\t¿Desea modificar un registro?(S/n): ")
            break
        Menu()

    elif opcion == 4:

        Cliente.cantidad_Clientes()

    else:

        try:

            print("\t" + "-"*40)
            print("\tIngrese una opcion correcta\n")
        except:
            pass

    opcion = int(input("\t\tOpcion: "))

print("\t" + "-" * 42)
print("\t|\t  ¡Gracias por usar mi programa!\t |")
print("\t" + "-" * 42)