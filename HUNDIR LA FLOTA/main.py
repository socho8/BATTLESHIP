from variables import tablero_jugador, tablero_maquina, tablero_intentos_jugador, tablero_intentos_maquina
from funciones import colocar_barcos_jugador, colocar_barcos_maquina,imprimir_tablero, obtener_posicion_barco, validar_disparo
from variables import barcos
from random import randint
import numpy as np


# Inicio del juego
print("¡Bienvenido al juego de Hundir la flota!")
nombre_jugador = input("Por favor, ingresa tu nombre: ")
print(input("¿Que edad tienes?"))
print(f"""\nHola {nombre_jugador}.\n
      El objetivo del juego es hundir todos los barcos de la máquina antes de que ella hunda los tuyos.\n
      Tienes que elegir coordenadas (fila y columna) para disparar a los barcos de la máquina.\n
      El tablero se representa con  y filas etiquetadas de A a J ycolumnas numeradas del 1 al 10.\n
      Si tu disparo impacta en un barco, se marcará como 'X'. Si no, se marcará como '-'.\n
      ¡Buena suerte!\n""")
input("Presiona Enter para comenzar...")

# Colocar barcos en los tableros de jugador y máquina
colocar_barcos_jugador(tablero_jugador)
colocar_barcos_maquina(tablero_maquina)

while True:
    # Turno del jugador
    while True:
        print("Turno del jugador")
        print("Introduzca coordenadas")
        imprimir_tablero(tablero_intentos_jugador)
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
