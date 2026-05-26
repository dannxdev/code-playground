# Problema 4: Se necesita elaborar una aplicación que permita capturar
# por teclado 9 números que se deben almacenar en una matriz de 3 × 3
# números que estén en el rango entre 100 y 200 ambos incluidos.
# Con la información se debe establecer cuál es la suma total y el promedio
# de las 2 diagonales principales de la matriz y cuál de ellas obtiene el
# resultado mayor y el mejor promedio (la que inicia en la posición (0,0) o
# la que inicia en la posición (0,4).
# Por pantalla se debe mostrar la matriz con la información y la suma total
# de cada una de las 2 diagonales indicando cuál fue la que obtuvo el mayor
# resultado.

import os

os.system('cls')

matriz_3x3_ejemplo = [[125, 126, 127], [128, 129, 130], [180, 179, 178]]


def crear_matriz_3x3():
    matriz_3x3 = []
    lista = []
    for i in range(1, 10):
        print(f"NUMERO {i}:")
        while True:
            numero_usuario = input("Escriba un numero entre 100 - 200: ")
            try:
                numero_usuario = int(numero_usuario)
                if 100 <= numero_usuario <= 200:
                    lista.append(numero_usuario)
                    break
                print("El numero esta fuera del rango establecido.")
            except ValueError:
                print("Ingrese solo numeros por favor.")
        if len(lista) == 3:
            matriz_3x3.append(lista)
            lista = []

    return matriz_3x3


def calcular_diagonales_matriz(matriz_3x3):
    print("RESULTADOS:\n")

    diagonal_1 = []
    diagonal_2 = []

    for x in range(3):
        diagonal_1.append(matriz_3x3[x][x])

    z = 2
    for y in range(3):
        diagonal_2.append(matriz_3x3[y][z])
        z -= 1

    suma_diagonal_1 = sum(diagonal_1)
    suma_diagonal_2 = sum(diagonal_2)

    promedio_diagonal_1 = round(suma_diagonal_1 / len(diagonal_1), 2)
    promedio_diagonal_2 = round(suma_diagonal_2 / len(diagonal_2), 2)

    if suma_diagonal_1 > suma_diagonal_2:
        print(
            f"La SUMA de la diagonal {diagonal_1}: {suma_diagonal_1}, es mayor que la SUMA de la diagonal {diagonal_2}: {suma_diagonal_2}.")
    else:
        print(
            f"La SUMA de la diagonal {diagonal_2}: {suma_diagonal_2}, es mayor que la SUMA de la diagonal {diagonal_1}: {suma_diagonal_1}.")

    if promedio_diagonal_1 > promedio_diagonal_2:
        print(
            f"El PROMEDIO de la diagonal {diagonal_1}: {promedio_diagonal_1}, es mayor que el PROMEDIO de la diagonal {diagonal_2}: {promedio_diagonal_2}.")
    else:
        print(
            f"El PROMEDIO de la diagonal {diagonal_2}: {promedio_diagonal_2}, es mayor que el PROMEDIO de la diagonal {diagonal_1}: {promedio_diagonal_1}.")


def mostrar_matriz(matriz: list):

    print("\nMATRIZ GENERADA:\n")
    for x in matriz:
        print(x)
    print("\n")


# mostrar_matriz(matriz_3x3_ejemplo)
# calcular_diagonales_matriz(matriz_3x3_ejemplo)

matriz_3x3_nueva = crear_matriz_3x3()
mostrar_matriz(matriz_3x3_nueva)
calcular_diagonales_matriz(matriz_3x3_nueva)

input("\nPresione ENTER para cerrar...\n")
