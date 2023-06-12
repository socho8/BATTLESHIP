import numpy as np
import random
from random import randint

# Diccionario de los barcos y sus tamaños
barcos = {
    'Barco4': 4,
    'Barco31': 3,
    'Barco32': 3,
    'Barco21': 2,
    'Barco22': 2,
    'Barco23': 2,
    'Barco11': 1,
    'Barco12': 1,
    'Barco13': 1,
    'Barco14': 1
}

# Tableros de juego
tablero_jugador = np.full((10, 10), " ")
tablero_maquina = np.full((10, 10), " ")
tablero_intentos_jugador = np.full((10, 10), " ")
tablero_intentos_maquina = np.full((10, 10), " ")

def print_board(tablero):
    print("   A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+-+")
    numero_filas = 1
    for filas in tablero:
        print("%2d|%s|" % (numero_filas, "|".join(filas)))
        numero_filas += 1

numero_a_letras = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9
}

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

def colocar_barcos_jugador(tablero):
    for barco, tamaño in barcos.items():
        while True:
            print_board(tablero)
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
        print_board(tablero)
        print(f"El {barco} fue colocado correctamente.")

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

# Colocar barcos en los tableros de jugador y máquina
colocar_barcos_jugador(tablero_jugador)
colocar_barcos_maquina(tablero_maquina)

while True:
    # Turno del jugador
    while True:
        print("Turno del jugador")
        print("Introduzca coordenadas")
        print_board(tablero_intentos_jugador)
        fila, columna = obtener_posicion_barco()
        if validar_disparo(fila, columna, tablero_maquina, tablero_intentos_jugador):
            break

    if np.count_nonzero(tablero_intentos_jugador == "X") == sum(barcos.values()):
        print("¡Felicidades! Hundiste todos los barcos. ¡Ganaste!")
        break

    # Turno de la máquina
    while True:
        print("Turno de la computadora")
        fila, columna = randint(0, 9), randint(0, 9)
        if validar_disparo(fila, columna, tablero_jugador, tablero_intentos_maquina):
            break

    if np.count_nonzero(tablero_intentos_maquina == "X") == sum(barcos.values()):
        print("Lo siento, la máquina hundió todos tus barcos. ¡Perdiste!")
        break
