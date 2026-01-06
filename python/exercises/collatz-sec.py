import os

# Borra la consola cada vez que se ejecuta el codigo:
os.system('cls')


# CONJETURA DE COLLATZ
def collatz(num):
    """Recibe solamente un numero entero positivo. 
    Si el numero es par: num = num/2,
    Si es impar: num = (num*3)+1.
    Imprime una secuencia de numeros y se detiene cuando el numero es 1."""

    # Si el numero = 1 detiene el bucle infinito que genera la recursividad.
    if num == 1:
        print(num)

    else:
        print(num)
        # Si el numero es par se divide entre 2
        if num % 2 == 0:
            num = num/2
            # La funcion se llama a si misma para verificar el nuevo numero:
            collatz(num)
        # Si el numero es impar se multiplica por 3 y se suma 1
        else:
            num = (num*3)+1
            # La funcion se llama a si misma para verificar el nuevo numero:
            collatz(num)


collatz(1024)
