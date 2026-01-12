# Problema 3: Se solicita la creación de una aplicación que elabore una
# matriz de 4 × 4 en la cual se almacenarán números entre el 3 y el 6
# ambos incluidos que se deben capturar por teclado.
# Una vez obtenida la información se debe establecer cuantas veces se
# repiten cada uno de los números del 3 al 6 y hallar la potencia de ellos de
# acuerdo con las veces que se repita.
# Se debe mostrar por pantalla la matriz generada y las potencias de los 4
# números.

import os

os.system('cls')

matriz_4x4_ejemplo = [[4, 6, 3, 3], [5, 4, 3, 3], [5, 5, 4, 6], [5, 4, 3, 6]]


def crear_matriz_4x4():
    matriz_4x4 = []
    lista = []
    for i in range(1, 17):
        print(f"NUMERO {i}:")
        while True:
            numero_usuario = input("Escriba un numero entre 3 - 6: ")
            try:
                numero_usuario = int(numero_usuario)
                if 3 <= numero_usuario <= 6:
                    lista.append(numero_usuario)
                    break
                print("El numero esta fuera del rango establecido.")
            except ValueError:
                print("Ingrese solo numeros por favor.")
        if len(lista) == 4:
            matriz_4x4.append(lista)
            lista = []

    return matriz_4x4


def mostrar_matriz(matriz: list):

    print("\nMATRIZ GENERADA:\n")
    for x in matriz:
        print(x)
    print("\n")


def hallar_potencia_matriz(matriz_4x4):
    print("RESULTADOS:\n")
    numeros_3_al_6 = {num: 0 for num in range(3, 7)}

    for fila in matriz_4x4:
        for num in fila:
            numeros_3_al_6[num] += 1

    for n, c in numeros_3_al_6.items():
        print(f"- {n}^{c} = {n**c}")


matriz_4x4_nueva = crear_matriz_4x4()
mostrar_matriz(matriz_4x4_nueva)
hallar_potencia_matriz(matriz_4x4_nueva)

input("\nPresione ENTER para cerrar...\n")
