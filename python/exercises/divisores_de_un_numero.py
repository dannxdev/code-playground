# Solicitar por teclado un número entero positivo y luego obtener, del número capturado, sus divisores
# y la cantidad de ellos. Debe mostrar por pantalla todos los divisores y la
# cantidad de ellos.

import os
os.system('cls')


def divisores_de_un_numero(num) -> dict:
    """
    Calcula el numero de divisores de un numero n y cuales son.
    """

    divisores = []
    for n in range(1, num+1):
        if num % n == 0:
            divisores.append(n)
    print(
        f"\nResultados:\n\nNumero: {num}\nDivisores: {divisores}\nCantidad: {len(divisores)}\n")
    return {num: {"divisores": divisores, "cantidad": len(divisores)}}


if __name__ == "__main__":
    print("========================================")
    print("      Calculadora de Divisores      ")
    print("========================================\n")
    while True:
        numero_usuario = input("Escriba un numero de 2 a 100: ")
        try:
            numero_usuario = int(numero_usuario)
            if 2 <= numero_usuario <= 100:
                divisores_de_un_numero(numero_usuario)
                break
            print("Numero fuera del rango. Ingrese otro numero.")
        except ValueError:
            print("Ingrese solo numeros, por favor.")

    input("\nPresione Enter para salir...\n")
