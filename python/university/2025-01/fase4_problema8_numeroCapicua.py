# Problema 8: Hacer un programa en python utilizando funciones, que
# lea un número entero positivo de cualquier cantidad de dígitos (cifras)
# que averigüe e imprima lo siguiente:
# Si la cantidad de cifras es impar averiguar si el número es capicúa
# Ejemplo: 585, 25352 y si la cantidad de cifras es par averiguar si el
# número es múltiplo de 4 y termina en 8, Ejemplo = 28
# Realizar siguientes funciones:
# • Función cifras par impar: Recibe como parámetro el número y
# retorna 1 si la cantidad de cifras es impar y retorna 0 si la
# cantidad de cifras es par.
# • Función capicúa: Recibe como parámetro el número cuya
# cantidad de dígitos sea impar, retorna 1 si el número es
# capicúa y retorna 0 si el número no es capicúa.
# • Función múltiplo: Que recibe como parámetro el número cuya
# cantidad de dígitos sea par y que calcule e imprima si el
# número es múltiplo de 4 y termina en 8. EJ = 28
# • Función main: Ingresa un número entero positivo realiza el
# llamado a la función cifras par impar, si es impar el llamado a la
# función capicúa y muestra si el número es capicúa o no es
# capicúa, de lo contrario realiza el llamado a la función
# múltiplo.

import os
os.system('cls')


def cant_cifras_es_par(num: int):
    """
    Determina si la cantidad de cifras de un numero es par (True) o no (False).
    """

    if len(str(num)) % 2 == 0:
        return True
    return False


def es_capicua(num: int):
    """
    Determina si un numero es capicua (Se escribe igual al contrario).
    """

    reversed_num = int(str(num)[::-1])
    return num == reversed_num


def es_multiplo_de_4(num: int):
    """
    Determina si el numero es múltiplo de 4 y termina en 8.
    """
    return num % 4 == 0 and int(str(num)[-1]) == 8


def main():
    """
    programa principal.
    """
    while True:
        try:
            num_usuario = int(
                input("\nEscriba un numero (Digite 0 para salir): "))
            if num_usuario > 0:
                if cant_cifras_es_par(num_usuario):
                    if es_multiplo_de_4(num_usuario):
                        print(
                            f"\nCant. Cifras Par: El numero {num_usuario} ES múltiplo de 4 y termina en 8.")
                    print(
                        f"\nCant. Cifras Par: El numero {num_usuario} NO ES múltiplo de 4 o NO termina en 8.")

                else:
                    if es_capicua(num_usuario):
                        print(
                            f"\nCant. Cifras Impar: El numero {num_usuario} ES Capicua.")
                    print(
                        f"\nCant. Cifras Impar: El numero {num_usuario} NO ES Capicua.")
            elif num_usuario == 0:
                break

            else:
                print("Ingrese un numero entero mayor a cero.")

        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    main()
