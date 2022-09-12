#Definiciones

from math import inf
import logging
import datetime

logging.basicConfig(filename='LOG.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
pila = []

def log_info(text):
    x = datetime.datetime.now()
    logging.info(str(x)+"  -"+text)

def log_error(text):
    x = datetime.datetime.now()
    logging.error(str(x)+"  -"+text)


def input_stack():
    print("Ingrese un texto para agregar a la pila: ")
    texto = input()
    pila.append(texto)
    print("Texto ingresado en la pila!")
    log_info("---Texto agregado a la pila")

def print_stack():
    toPrint = ""
    n = len(pila)
    for i in range(n):
        print("["+str(i)+"] - Texto "+str(i))
    try:
        toPrint = int(input("\nElija cual texto de la pila desea imprimir: "))
    except:
        log_error("[ERROR] Opcion invalida")
        print("****Opcion no válida. Por favor intente nuevamente.****")
    if (toPrint not in range(n)):
        log_error("[ERROR] Opcion invalida")
        print("****Opcion no válida. Por favor intente nuevamente.****")
    else:
        print("Texto impreso de la pila: ", pila[toPrint])
        log_info("---Texto impreso")

def menu_largos():
    n = len(pila)
    size_aux = 0
    size_array = [0]
    opcion = ""

    if (n == 1):
        print("La pila contiene solo un texto, el cual corresponde a : ", pila[0])
    else:
        while (True):
            log_info("[Menu] Menu Largos de pila")
            print("\n-MENU TAMAÑOS PILA-")
            print("[0] - Volver al menu anterior")
            print("[1] - Texto más largo de la pila.")
            print("[2] - Texto más corto de la pila.")
            try:
                opcion = int(input("\nElija una opcion: "))
            except:
                log_error("[ERROR] Opcion invalida")
                print("****Opcion no válida. Por favor intente nuevamente.****")
                continue
            if (opcion == 0):
                log_info("[Opcion] Volver al menu pila")
                break
            elif (opcion == 1): #Verificar el mas largo
                log_info("[Opcion] Obtener texto mas largo")
                size_aux = 0
                for text in pila: #Encontrar el mas largo inicialmente
                    largo = len(text)
                    if (largo > size_aux):
                        size_array[0] = text
                        size_aux = largo
                for text in pila: #Revisar si hay mas textos del mismo largo
                    largo = len(text)
                    if ((largo == size_aux) and (text not in size_array)):
                        size_array.append(text)
                if (len(size_array) == 1):
                    log_info("---Se obtuvo el texto más largo")
                    print("El texto más largo es: ", size_array[0])
                else:
                    log_info("---Se obtuvieron los textos más largos")
                    print("Los textos mas largos (del mismo tamaño) son: ", size_array)

            elif (opcion == 2): #Verificar el mas corto
                log_info("[Opcion] Obtener texto mas corto")
                size_aux = inf
                for text in pila: #Encontrar el mas corto inicialmente
                    largo = len(text)
                    if (largo < size_aux):
                        size_array[0] = text
                        size_aux = largo
                for text in pila: #Revisar si hay mas textos del mismo largo
                    largo = len(text)
                    if ((largo == size_aux) and (text not in size_array)):
                        size_array.append(text)
                if (len(size_array) == 1):
                    log_info("---Se obtuvo el texto más corto")
                    print("El texto más corto es: ", size_array[0])
                else:
                    log_info("---Se obtuvieron los textos más cortos")
                    print("Los textos mas cortos (del mismo tamaño) son: ", size_array)

            print("------------------------------------")

def menu_comparar():
    while(True):
        log_info("[Menu] Menu Comparacion")
        opcion1 = ""
        opcion2 = ""
        n = len(pila)
        print("\n-MENU COMPARACION PILA-")
        for i in range(n):
            print("["+str(i)+"] - Texto "+str(i))
        try:
            opcion1 = int(input("\nElija el primer texto a comparar: "))
        except:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue
        if (opcion1 not in range(n)):
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue
        log_info("---Primer texto seleccionado")
        for i in range(n):
            if (i != opcion1):
                print("["+str(i)+"] - Texto "+str(i))
        try:
            opcion2 = int(input("\nElija el segundo texta con el que se va a comparar: "))
        except:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue
        if (opcion2 not in range(n)):
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue
        log_info("---Segundo texto seleccionado")
        if(opcion1 == opcion2):
            log_error("[ERROR] Opcion invalida")
            print("****No puede elegir el mismo texto dos veces. Intente nuevamente****")
        elif((opcion1 or opcion2) not in range(n)):
            log_error("[ERROR] Opcion invalida")
            print("****Debe escoger las opciones que se muestran. Intente nuevamente****")
        else:
            largo1 = len(pila[opcion1])
            largo2 = len(pila[opcion2])
            if(largo1 > largo2):
                log_info("---Primer texto más largo")
                print("El primer texto ["+str(opcion1)+"] es mas largo que el segundo texto ["+str(opcion2)+"]")
            elif(largo1 < largo2):
                log_info("---Segundo texto más largo")
                print("El segundo texto ["+str(opcion2)+"] es mas largo que el primer texto ["+str(opcion1)+"]")
            else:
                log_info("---Ambos textos igual de largos")
                print("Ambos textos son igual de largos")
            break

def menu_pila():
    while (True):
        log_info("[Menu] Menu Pila")
        opcion = ""
        print("\n-MENU PILA-")
        print("[0] - Salir del programa")
        print("[1] - Agregar un texto a la pila.")
        print("[2] - Imprimir texto de la pila.")
        if (len(pila) > 1):
            print("[3] - Comparar textos de pila.")
        print("[4] - Cual es el texto mas largo y el mas corto de la pila.")

        try:
            opcion = int(input("\nElija una opcion: "))
        except:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue
        if (opcion == 0):
            log_info("[Opcion] Salir del programa")
            quit()
        elif (opcion == 1):
            log_info("[Opcion] Agregar texto a pila")
            input_stack()
        elif (opcion == 2):
            log_info("[Opcion] Imprimir texto de pila")
            print_stack()
        elif (opcion == 3 and len(pila) > 1):
            log_info("[Opcion] Comparar textos de pila")
            menu_comparar()
        elif (opcion == 4):
            log_info("[Opcion] Obtener textos mas largos y cortos")
            menu_largos()
        else:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
        
        print("------------------------------------")


def menu_principal():
    while (True):
        log_info("[Menu] Menu Principal")
        opcion = ""
        print("\n-MENU-")
        print("[0] - Salir del programa")
        print("[1] - Agregar un texto a la pila.")
        if (len(pila) > 0):
            print("[2] - Comandos de la pila")
        try:
            opcion = int(input("\nElija una opcion: "))
        except:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")
            continue

        if (opcion == 0):
            log_info("[Opcion] Salir del programa")
            quit()
        elif (opcion == 1):
            log_info("[Opcion] Agregar texto a pila")
            input_stack()
        elif (opcion == 2 and len(pila) > 0):
            log_info("[Opcion] Menu de pila")
            menu_pila()
        else:
            log_error("[ERROR] Opcion invalida")
            print("****Opcion no válida. Por favor intente nuevamente.****")

        print("------------------------------------")
        

#Main
print("\n--Bienvenido al sistema de textos de una pila--")
log_info("---Inicio de Programa")
menu_principal()