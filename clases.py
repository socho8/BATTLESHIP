import random
import numpy as np
from variables import barcos, numero_a_letras

#Imprimir tabler
def imprimir_tablero(tablero):
    print("   A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+-+")
    numero_filas = 1
    for filas in tablero:
        print("%2d|%s|" % (numero_filas, "|".join(filas)))
        numero_filas += 1
    
#Obtener las posiciones de los barcos
def obtener_posicion_barco():
    while True:
        try:
            posicion = input("Introduca coordenada (ej: A1): ").upper()
            if len(posicion) == 2 and posicion[0] in 'ABCDEFGHIJ' and posicion[1] in '12345678910':
                fila = int(posicion[1]) - 1
                columna = numero_a_letras[posicion[0]]
                break
        except (ValueError, KeyError):
            print("Posicion invalida, intentalo nuevamente. (ej: A1).")
    return fila, columna

#Colocar manualmente los barcos 
def colocar_barcos_jugador(tablero):
    for barco, tamaño in barcos.items():
        while True:
            imprimir_tablero(tablero)
            print(f"Colocando {barco} (con un tamaño de {tamaño} esloras)")
            fila_barco, columna_barco = obtener_posicion_barco()
            if tablero[fila_barco][columna_barco] == " ":
                # Horizontal o vertical
                direccion = input("Introduzca una direccion (H para horinztoal y V para vertical): ").upper()
                if direccion == "H":
                    if columna_barco + tamaño <= 10 and all(tablero[fila_barco][columna_barco + i] == " " for i in range(tamaño)):
                        for i in range(tamaño):
                            tablero[fila_barco][columna_barco + i] = "O"
                        break
                    else:
                        print("Posicion invalida, intentalo nuevamente.")
                elif direccion == "V":
                    if fila_barco + tamaño <= 10 and all(tablero[fila_barco + i][columna_barco] == " " for i in range(tamaño)):
                        for i in range(tamaño):
                            tablero[fila_barco + i][columna_barco] = "O"
                        break
                    else:
                        print("Posicion invalida, intentalo nuevamente.")
                else:
                    print("Posicion invalida, intentalo nuevamente.")
            else:
                print("Esta opcion ya fue tomada, intentalo nuevamente")
        imprimir_tablero(tablero)
        print(f"El {barco} fue colocado correctamente.")

#Colocar aleatoreamente los barcos de la maquina
def colocar_barcos_maquina(tablero):
    for barco, tamaño in barcos.items():
        while True:
            fila_barco = random.randint(0, 9)
            columna_barco = random.randint(0, 9)
            direccion = random.choice(["H", "V"])
            if direccion == "H":
                if columna_barco + tamaño <= 10 and all(tablero[fila_barco][columna_barco + i] == " " for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila_barco][columna_barco + i] = "O"
                    break
            elif direccion == "V":
                if fila_barco + tamaño <= 10 and all(tablero[fila_barco + i][columna_barco] == " " for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila_barco + i][columna_barco] = "O"
                    break

#Comprobar disparo
def validar_disparo(fila, columna, tablero_barcos, tablero_intentos):
    if tablero_intentos[fila][columna] != " ":
        print("Ya has disparado en esta posicion. Intenta nuevamente.")
        return False
    elif tablero_barcos[fila][columna] == "O":
        print("¡Le diste a un barco!")
        tablero_intentos[fila][columna] = "X"
        tablero_barcos[fila][columna] = "X"
        return True
    else:
        print("Disparo al agua.")
        tablero_intentos[fila][columna] = "-"
        return True