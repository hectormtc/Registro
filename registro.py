#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
lista_Clientes = []

#Guarda la suma de cantidad de clientes
numero = 0

def Menu():
    print("\n\t" + "-" * 42)
    print("""\
        SISTEMA DE REGISTRO

        Opciones:

        1) Crear nuevo cliente
        2) Buscar Clientes
        3) Modificar registro
        4) Cantidad de Clientes
        0) Salir\
    """)
    print("\t" + "-" * 42)


#Pide la opcion para poder continuar con el programa
Menu()

opcion = int(input("\t\tOpcion: "))


class Cliente(object):
    """ Clase que contiene los establecimientos y las modificaciones"""
    def __init__(self, contra, nombre, sexo, edad, telefono, numero):

        self.contra = contra
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.telefono = telefono
        self.numero = numero


    def imprimir_Datos(self): #Imprime los datos una vez guardados

        print("\tContraseña: " + self.contra +
              '{}'.format("."))
        print("\tNombre: " + Cliente.obtener_Nombre(self) +
              '{}'.format("."))
        print("\tSexo: " + Cliente.obtener_sexo(self) +
              '{}'.format("."))
        print("\tEdad: " + Cliente.obtener_edad(self) +
              '{}'.format(" años"))
        print("\tTelefono: " + Cliente.obtener_telefono(self) +
              '{}'.format("."))

    def crearDatos(self):

        self.contra = input("\tContraseña: ")
        self.nombre = input("\tNombre: ")
        self.sexo = input("\tMujer/Hombre: ")
        self.edad = input("\tEdad: ")
        self.telefono = input("\tTelefono: ")

    def establecer_Modificacion(self):

        print("\n\tContraseña Generada: ",
              FuncionesCliente.generador_Contra(), "\n")
        Cliente.crearDatos(self)

    def obtener_Nombre(self):

        return self.nombre

    def obtener_edad(self):

        return self.edad

    def obtener_sexo(self):

        return self.sexo

    def obtener_telefono(self):
        base = self.telefono[:4]
        final = self.telefono[4:]
        telefono = base + "-" + final
        return telefono


class FuncionesCliente(Cliente):

    def validarRegistro(self):
        validacion = input("\n\t¿Crear registro registro(S/n)?: ")

        while validacion != "S":

            if validacion == "n":
                print("\n\tContraseña Generada: ",
                      FuncionesCliente.generador_Contra(), "\n")

                Cliente.crearDatos(self)

                validacion = input("\n\t¿Crear registro(S/n)?: ")
            else:
                print("\n\tSolo "'S'" o "'n'" ")
                validacion = input("\n\t¿Crear registro(S/n)?: ")

    def modificar_Registro(self):

        pregunta_Busqueda = int(input("\n\tIngrese su id: cliente_"))

        try:
            # Busca si el cliente se encuentra en la lista
            if lista_Clientes[pregunta_Busqueda]:

                print("\n\tNombre: " +
                      lista_Clientes[pregunta_Busqueda].nombre + '{}'.format("."))

                pregunta_Modificar = input("\n\t¿Desea modificar este registro?(S/n): ")

                while pregunta_Modificar != "n":

                    if pregunta_Modificar == "S":

                        lista_Clientes[pregunta_Busqueda].establecer_Modificacion()
                        print("\n\t¡Cliente Modificado Satisfactoriamente!")
                        return
                    else:

                        print("\n\tSolo S o n")
                    pregunta_Modificar = input("\n\t¿Desea modificar este registro?(S/n): ")

            else:
                pass
        except:
            print ("\n\t¡Cliente no encontrado!\n")

    def generador_Contra():
        # Genera una contraseña random entre 1000 y 9000
        return random.randint(1000, 9999)

    def crear(self):
        # Llama a la funcion generador_Id()
        print("\n\tContraseña Generada: ", FuncionesCliente.generador_Contra(), "\n")
        # Se crea la variable nuevo_cliente para heredar la clase Cliente()
        nuevo_cliente = Cliente()

        Cliente.crearDatos(self)

        # Se agrega esa nueva variable a la lista, lista_Clientes
        lista_Clientes.append(nuevo_cliente)

        print("\n\t¡Cliente agregado satisfactoriamente!\n")

    def buscar():
        # El id del cliente es el numero que dio al incio "cliente_"
        print ("\n\tIngrese su ID")
        buscar = int(input("\n\tID: cliente_"))

        try:
            if lista_Clientes[buscar]:

                lista_Clientes[buscar].imprimir_Datos()
            else:

                print("\n\tID encontrada\n")
                # Imprime los datos del cliente
        except:

            print("\n\tID no encontrada\n")

    def cantidad_Clientes(self):

        print ("\n\tCantidad de clientes: ", len(lista_Clientes), "\n")
        Menu()

########################################################################################################################


while opcion != 0: #Opciones para el Menu

    if opcion == 1: #Crear Nuevo Usuario

        print("\t"+"-"*40)
        # Cuando se crea un nuevo cliente, se suma 1 para indicar el id del cliente nuevo.
        numero += 1
        # Se crea la variable que va a mostrar el nuevo cliente
        nuevo_cliente = "cliente_" + str(int(numero-1))
        # Imprime el id del nuevo cliente
        print("\n\tID del Cliente: "+ nuevo_cliente)
        # Llama a la funcion de crear un nuevo cliente para ser guardado en la lista.
        FuncionesCliente.crear()

        Menu()
    elif opcion == 2: # Busca al cliente
        #Si la lista de clientes esta vacia imprimir:
        if len(lista_Clientes[:]) == 0:

            print("\n\tNo hay Clientes aun\n")
            Menu()
        else:
            pass
        #Siempre que existan clientes en la lista
        while len(lista_Clientes[:]) > 0:

            print("\t" + "-"*40)
            FuncionesCliente.buscar()
            Menu()

            break

    elif opcion == 3: #Modificar registro

        if len(lista_Clientes[:]) == 0:

            print("\n\tNo hay Clientes aun\n")

        else:
            pass

        while len(lista_Clientes[:]) > 0:

            print("\t" + "-"*40)

            FuncionesCliente.modificar_Registro()
            Menu()

    elif opcion == 4: #Cantidad de Clientes

        FuncionesCliente.cantidad_Clientes()

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
