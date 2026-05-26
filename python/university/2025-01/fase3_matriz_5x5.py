# Problema 2: Se requiere una aplicación que permita almacenar en un
# matriz de 5 × 5 25 números que se encuentren entre el rango de 10 a
# 90, estos números deben ser digitados por el usuario.
# Con la información obtenida se debe establecer cuál es la suma y el
# promedio de las celdas que componen el borde de la matriz (perímetro).
# Se debe mostrar por pantalla la matriz generada y el resultado de la suma
# y el promedio.

import os

os.system('cls')

matriz_ejemplo = [[30, 25, 17, 16, 32], [10, 56, 11, 14, 89], [
    47, 11, 13, 45, 65], [10, 19, 18, 17, 16], [15, 17, 16, 15, 20]]


def crear_matriz_5x5():
    matriz_5x5 = []
    lista = []
    for i in range(1, 26):
        print(f"NUMERO {i}:")
        while True:
            numero_usuario = input("Escriba un numero de 10 a 90: ")
            try:
                numero_usuario = int(numero_usuario)
                if 10 <= numero_usuario <= 90:
                    lista.append(numero_usuario)
                    break
                print("El numero esta fuera del rango establecido.")
            except ValueError:
                print("Ingrese solo numeros por favor.")
        if len(lista) == 5:
            matriz_5x5.append(lista)
            lista = []

    return matriz_5x5


def calcular_suma_promedio_matriz(matriz):
    valores_bordes = []

    i = 0
    for fila in matriz:
        if i in (0, 4):

            for num in fila:
                valores_bordes.append(num)
        else:
            valores_bordes.append(fila[0])
            valores_bordes.append(fila[4])
        i += 1

    perimetro = sum(valores_bordes)
    promedio = round(perimetro / len(valores_bordes), 2)

    print(
        f"RESULTADOS:\n\nEl Perimetro de la matriz es {perimetro}.\nEl promedio de los valores del borde de la matriz es {promedio}.")


def mostrar_matriz(matriz: list):

    print("\nMATRIZ GENERADA:\n")
    for x in matriz:
        print(x)
    print("\n")


matriz_nueva = crear_matriz_5x5()
mostrar_matriz(matriz_nueva)
calcular_suma_promedio_matriz(matriz_nueva)

# mostrar_matriz(matriz_ejemplo)
# calcular_suma_promedio_matriz(matriz_ejemplo)

input("\nPresione Enter para salir: ")
