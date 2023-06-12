import numpy as np

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


#Transformacion de numeros a letras
numero_a_letras = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9
}