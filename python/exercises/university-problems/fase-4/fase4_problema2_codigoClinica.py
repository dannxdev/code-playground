import os

os.system('cls')

# Creando un diccionario con los servicios y sus costos:
servicios = {
    1: {"RADIOGRAFIA": 30000},
    2: {"ECOGRAFIA": 35000},
    3: {"LABORATORIO": 25000},
    4: {"CONSULTA EXTERNA": 40000},
    5: {"CONSULTA ESPECIALIZADA": 80000}
}


def validar_codigo(codigo: int):
    """
    Recibe como parámetro un número entero, retorna True sí 
    el número tiene 5 dígitos, en caso de no cumplir retorna False, 
    para indicar que no es válido
    """
    # Validando si el codigo ingresado es entero:
    if isinstance(codigo, int):
        if len(str(codigo)) == 5 and codigo > 0:
            # Si el numero contiene 5 digitos:
            return True
    return False


def tipo(codigo: int):
    """
    Recibe como parámetro un número entero, sí el primer dígito es 1 
    retorna "AFILIADO", pero sí es 2 retorna "PARTICULAR", 
    dato de tipo string. 
    """

    if int(str(codigo)[0]) == 1:
        # Si el primer digito del codigo es 1:
        return "AFILIADO"
    if int(str(codigo)[0]) == 2:
        # Si el primer dgito del codigo es 2:
        return "PARTICULAR"
    # Si el primer digito es un numero diferente a los anteriores:
    return "TIPO NO DEFINIDO"


def servicio(codigo: int):
    """
    Recibe como parámetro un número entero, el segundo dígito permite 
    retornar el nombre del procedimiento a realizar.
    Ejemplo: sí el dígito es 3 retorna "LABORATORIO" 
    """
    if not tipo(codigo) == "TIPO NO DEFINIDO":
        # Extrayendo el segundo digito del codigo:
        segundo_digito = int(str(codigo)[1])
        # Extrayendo el servicio asociado a ese digito {servicio: costo}:
        resultado = servicios.get(segundo_digito)

        if resultado is not None:
            # Si encontro un servicio asocado a ese digito:
            for s in resultado:
                # Retorna la clave (sevicio)
                return s
    # Si nada de lo anterior se cumple:
    return "SERVICIO NO DEFINIDO"


def costo(nombre_servicio: str):
    """
    Recibe como parámetro un dato de tipo string con el nombre del servicio 
    a realizar, con base a este se determinar el costo base. 
    Ejemplo: sí recibe "LABORATORIO" se retorna 25000. 
    """

    # Si el servicio dado como argumento es un string:
    if isinstance(nombre_servicio, str):
        servicio_costos = {}

        # Iterando cada valor del diccionario:
        for s in servicios.values():
            # Iterando cada servicio-precio del diccionario:
            for nombre, precio in s.items():
                # Crea un nuevo diccionario con los valores {servicio: precio}:
                servicio_costos[nombre] = precio

        # Busca el nombre de servicio en el nuevo diccionario
        return servicio_costos.get(nombre_servicio, float(0))

    # Si no encuentra nada:
    return float(0)


def calcular_descuento_recargo(codigo: int, tipo_paciente: str, costo_servicio: int):
    """
    Recibe como parámetro un número entero (el código), un dato de tipo string 
    con el tipo de paciente y un dato de tipo entero con el costo del procedimiento, 
    y calcula el valor del descuento o recargo. 
    """

    # Crando ua lista donde se almacenaran los 3 digitos:
    ultimos_3_digitos = []

    codigo_string = str(codigo)

    # Iterando cada digito del codigo:
    for i in range(5):
        if i in (2, 3, 4):
            # Si el digito esta en la poscion 2, 3 o 4 (3 ultimos) se anaden a la lista:
            ultimos_3_digitos.append(int(codigo_string[i]))

    # Sumando los 3 ultimos digitos encontrados:
    suma_3_digitos = sum(ultimos_3_digitos)

    if suma_3_digitos % 2 == 0:
        # Si la suma es par:
        if tipo_paciente == "AFILIADO":
            return float(-(costo_servicio * 0.15))

        if tipo_paciente == "PARTICULAR":
            return float(costo_servicio * 0.15)

        return float(0)

    # Si la suma es impar:
    if tipo_paciente == "AFILIADO":
        return float(-(costo_servicio * 0.25))

    if tipo_paciente == "PARTICULAR":
        return float(costo_servicio * 0.25)

    return float(0)


def pago_total(costo_base: int, desc_rec: float):
    """
    Recibe como parámetro un número entero correspondiente al costo base 
    del servicio y un número float correspondiente al descuento o recargo 
    que se aplicara, la función retorna el valor final a pagar por el servicio. 
    """
    # Retorna la suma del costo base y la cantidad de descuento o recargo:
    return costo_base + desc_rec


def principal():
    """
    Programa principal, que ejecuta todas las funciones anteriores.
    """

    # Creando un bucle hasta que el codigo ingresado por teclado sea valido:
    while True:
        try:
            codigo_usuario = int(input("Ingrese su codigo de 5 digitos: "))
            if validar_codigo(codigo_usuario):
                break
            print("Error: El numero debe tener 5 digitos (no negativo).\n")
        except ValueError:
            print("Error: Ingrese solo numeros por favor.\n")

    # Almacenando en variables las llamadas a ls funciones:
    tipo_usuario = tipo(codigo_usuario)
    servicio_usuario = servicio(codigo_usuario)
    costo_servicio_usuario = costo(servicio_usuario)
    calculo_desc_rec = calcular_descuento_recargo(
        codigo_usuario, tipo_usuario, costo_servicio_usuario)
    total_a_pagar_usuario = pago_total(
        costo_servicio_usuario, calculo_desc_rec)

    # Mostrando los datos en pantalla:
    print("\nFACTURA PACIENTE\n")
    print(f"- Tipo: {tipo_usuario}")
    print(f"- Servicio: {servicio_usuario}")
    print(f"- Costo Servicio: {costo_servicio_usuario}")

    if calculo_desc_rec > 0:
        item = "Recargo"
    else:
        item = "Descuento"

    print(f"- Valor del {item}: {calculo_desc_rec}")
    print(f"\nTotal a pagar: {total_a_pagar_usuario}")


if __name__ == "__main__":
    print("========================================")
    print("      Problema 2: Codigo Servicio Clinica      ")
    print("========================================\n")
    principal()

    input("\nPresione ENTER para salir.\n")
