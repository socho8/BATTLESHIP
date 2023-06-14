from variables import tablero_jugador, tablero_maquina, tablero_intentos_jugador, tablero_intentos_maquina
from funciones import colocar_barcos_jugador, colocar_barcos_maquina,imprimir_tablero, obtener_posicion_barco, validar_disparo
from variables import barcos, numero_a_letras
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

print("Este es tu tablero generado aleatoriamente")
imprimir_tablero(tablero_jugador)


while True:
    
    # Turno del jugador
    while True:
        print("Turno del jugador")
        #imprimir_tablero(tablero_intentos_jugador)
        fila, columna = obtener_posicion_barco()
        if validar_disparo(fila, columna, tablero_maquina, tablero_intentos_jugador):
            break
        #print("Introduzca coordenadas")
        
        

    if np.count_nonzero(tablero_intentos_jugador == "X") == sum(barcos.values()):
        print("¡Felicidades! Hundiste todos los barcos. ¡Ganaste!")
        break

    # Turno de la máquina
    while True:
        print("Turno de la computadora")
        #imprimir_tablero(tablero_intentos_maquina)
        #imprimir_tablero(tablero_intentos_jugador)
        fila, columna = randint(0, 9), randint(0, 9)
        if fila =='ABCDEFGHIJ':
                fila = numero_a_letras[fila]
                print(f"La maquina disparo a las coordenadas {fila}{columna}")
        if validar_disparo(fila, columna, tablero_jugador, tablero_intentos_maquina):
            break
        #fila, columna = obtener_posicion_barco()


    print(" ")
    print("TABLERO DE LA MAQUINA")    
    imprimir_tablero(tablero_intentos_jugador)
    print(" ")
    print("TABLERO DEL JUGADOR",)
    imprimir_tablero(tablero_intentos_maquina)
    

    if np.count_nonzero(tablero_intentos_maquina == "X") == sum(barcos.values()):
        print("Lo siento, la máquina hundió todos tus barcos. ¡Perdiste!")
        break
