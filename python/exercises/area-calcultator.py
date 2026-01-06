def area_calculator():
    print("AREA CALCULTATOR")
    print("""Bienvenido, con este programa usted podra \ncalcular el area de:
    1. CUADRADO
    2. RECTANGULO
    3. TRIANGULO
    4. CIRCULO
    """)

    user_figure = int(input("Seleccione una opcion (1-4): "))

    if user_figure == 1:
        print("A elegido calcular el area de un cuadrado.")
        lado_cuadrado = float(
            input("¿Cuanto mide el lado de su cuadrado? (m): "))
        area_cuadrado = lado_cuadrado**2
        print(f"Area del cuadrado = {area_cuadrado} metros cuadrados")

    elif user_figure == 2:
        print("A elegido calcular el area de un Rectangulo.")
        base_rect = float(
            input("¿Cuanto mide la base de su rectangulo? (m): "))
        altura_rect = float(
            input("¿Cuanto mide la altura de su rectangulo? (m): "))
        area_rect = base_rect * altura_rect
        print(f"Area del rectangulo = {area_rect} metros cuadrados")

    elif user_figure == 3:
        print("A elegido calcular el area de un Triangulo.")
        base_trian = float(
            input("¿Cuanto mide la base de su Triangulo? (m): "))
        altura_trian = float(
            input("¿Cuanto mide la altura de su Triangulo? (m): "))
        area_trian = (base_trian * altura_trian)/2
        print(f"Area del triangulo = {area_trian} metros cuadrados")

    elif user_figure == 4:
        print("A elegido calcular el area de un Circulo.")
        radio = float(input("¿Cuanto mide el radio de su circulo? (m): "))
        area_circ = float(3.1416 * (radio**2))
        print(f"Area del circulo = {area_circ} metros cuadrados")


while True:
    pregunta = input("Desea intentarlo otra vez: ").lower()
    if pregunta == "si":
        area_calculator()

    elif pregunta == "no":
        print("Ud salio del programa")
        break
