import os
os.system("cls")


def caculadora_imc(peso: float, altura: float):
    """Recibe un peso y una altura decimales y calcula el indice de masa corporal"""
    imc = (peso)/(altura**2)
    imc = round(imc, 2)
    print(f"Su indice de masa corporal es : {imc}")

    if imc <= 19:
        print("Esta muy delgado")
    elif imc >= 20 and imc <= 25:
        print("Tiene un buen estado de salud")
    elif imc >= 30:
        print("Le recomiendo bajar de peso.")


while True:
    pregunta = input("Iniciar (Y/N): ").lower()
    if pregunta == "y":
        try:
            p = float(input("Escriba aqui su peso (Kg): "))
            a = float(input("Escriba aqui su altura (metros): "))
            caculadora_imc(p, a)
        except ValueError:
            print("Ingrese un valor valido")

    else:
        print("Saliendo...")
        break
