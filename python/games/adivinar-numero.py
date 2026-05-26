import random
import os

os.system("cls")


def sep():
    print('------------------------')


def adivinar_numero():
    print("Bien, numero pensado... Adivinalo!!!")
    numero = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        sep()
        user = int(
            input(f"Escribe aqui tu numero (tienes {intentos} intentos): "))
        sep()
        if user == numero:
            print("Haz adibinado el numero ¡FELICIDADES!")
            sep()
            break
        elif user > numero:
            if user > 20:
                sep()
                print("Recuerda que es un numero entre 1 y 20, ¡te pasaste!!!.")
                sep()
            else:
                sep()
                print("Muy alto")
                sep()
            intentos -= 1
        elif user < numero:
            sep()
            print("Muy bajo")
            sep()
            intentos -= 1
        print("Intentalo denuevo...")

    else:
        print("Se Te acabaron los intentos")


while True:
    print("ESTE PROGRAMA PENSARA EN UN NUMERO DEL 1 AL 20\n¿SERAS CAPAZ DE ADIVINARLO?")
    sep()
    pregunta = input("Quieres jugar(si/no): ").lower()
    sep()
    if pregunta == "si":
        adivinar_numero()
    elif pregunta == "no":
        print("Vuelve cuando quieras")
        break
    else:
        print("La opcion no existe")
