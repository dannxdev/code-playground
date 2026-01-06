# Problema 4: Programa para manejar la venta de pasajes: los costos,
# clases y destinos están dados de la siguiente manera:
# Destinos
# a. Cúcuta
# i. Primera clase: 20000
# ii. Segunda clase: 15000
# iii. Tercera clase: 12000
# b. Bucaramanga
# i. Primera clase: 30000
# ii. Segunda clase: 25000
# iii. Tercera clase: 20000
# c. Bochalema
# i. Primera clase: 10000
# ii. Segunda clase: 8000
# iii. Tercera clase:5000
# La empresa ofrece descuentos por cantidad de pasajes, así: menos
# de 5 pasajes 0%, 6 a 12 pasajes 10% y más de 12 20%.
# Realizar las siguientes funciones:
# 5
# • Menú (): Utilizado en el main (), funcionara hasta que el
# usuario de la opción 2.
# Encabezado del menú: Viajes
# Opción 1: Vender pasaje
# Opción 2: Salir
# ¿Cuál es su opción?
# • Datos (): La función no tiene parámetros, muestra las
# opciones de viaje, preguntando el destino, clase y la cantidad
# de pasajes, los cuales retorna. Valida que el destino sea:
# Cúcuta, Bucaramanga o Bochalema y que la clase este entre
# 1 y 3.
# • ValorPa (): La función recibe el destino y la clase y retorna
# el valor del pasaje.
# • Descu (): La función recibe la cantidad de pasajes a comprar
# y retorna el valor del descuento.
# • Pago (): La función recibe la cantidad de pasajes, el valor
# base del pasaje y el porcentaje de descuento y retorna el
# valor final a pagar.
# Al terminar indicar cuantos pasajes se vendieron para cada destino
# y cuánto dinero se recaudó en general.


import os

os.system('cls')

DB_NOMBRES = {
    1: "Cucuta",
    2: "Bucaramanga",
    3: "Bochalema"
}

DB_PASAJES = {
    1: {
        "C1": 20000,
        "C2": 15000,
        "C3": 12000
    },

    2: {
        "C1": 30000,
        "C2": 25000,
        "C3": 20000
    },

    3: {
        "C1": 10000,
        "C2": 8000,
        "C3": 5000
    }
}

DB_CANT_PASAJES = {
    1: {
        "C1": 0,
        "C2": 0,
        "C3": 0
    },
    2: {
        "C1": 0,
        "C2": 0,
        "C3": 0
    },
    3: {
        "C1": 0,
        "C2": 0,
        "C3": 0
    }

}


RECAUDOS = []


def menu_principal():
    print("=" * 30)
    print("SISTEMA DE VIAJES")
    print("=" * 30)

    print("\n1. Vender pasaje.\n2. Salir\n")

    while True:
        try:
            opcion = int(input("¿Cual es su opcion?: "))
            if opcion in (1, 2):
                return opcion
            print("Opcion no valida")
        except ValueError:
            print("Opcion no valida")


def datos():

    datos_destino = {"id": 0, "clase": 0}

    print("\nCOMPRA DE BOLETOS")
    print("\nEscoja un destino:\n\n1. Cucuta\n2. Bucaramanga\n3. Bochalema\n")

    while True:
        try:
            destino_opcion = int(input("Escriba el numero de destino (1-3): "))
            if destino_opcion in (1, 2, 3):
                datos_destino["id"] += destino_opcion
                break
            if destino_opcion == 0:
                break
            print("Opcion no valida")
        except ValueError:
            print("Opcion no valida")

    if destino_opcion:
        print(f"\nDestino elegido: {DB_NOMBRES[destino_opcion]}\n")
        for m, n in DB_PASAJES[destino_opcion].items():
            print(f"- {m}: ${n}")

        while True:
            try:
                clase_opcion = int(
                    input("\nEscriba el numero de clase (1-3): "))
                if clase_opcion in (1, 2, 3):
                    datos_destino["clase"] += clase_opcion
                    break
                if clase_opcion == 0:
                    break
                print("Opcion no valida")
            except ValueError:
                print("Opcion no valida")

    return datos_destino


def valor_pasaje(datos_destino: dict):

    id_destino = datos_destino['id']
    clase_destino = datos_destino['clase']

    if id_destino:
        clases = DB_PASAJES[id_destino]

        if clase_destino:
            clase_destino = "C" + str(clase_destino)
            return clases[clase_destino]
    return 0


def descuento(cant_pasajes: int):
    """
    La empresa ofrece descuentos por cantidad de pasajes, así: menos
    de 5 pasajes 0%, 6 a 12 pasajes 10% y más de 12 20%.
    """

    if cant_pasajes > 0:
        if cant_pasajes <= 5:
            return float(0)
        if 6 <= cant_pasajes <= 12:
            return 0.1
        return 0.2

    return float(0)


def pago(cant_pasajes: int, pago_pasaje: int, valor_descuento: float):
    """
    Calcula el total a pagar aplicando el descuento.
    """

    total_base = cant_pasajes * pago_pasaje
    monto_descuento = total_base * valor_descuento

    return total_base - monto_descuento


def registrar_venta(datos_destino, cant_pasajes):
    """
    Registra la venta de los boletos e la base de datos.
    """

    id_destino = datos_destino["id"]
    clase_destino = datos_destino["clase"]

    clase_destino = "C" + str(clase_destino)

    DB_CANT_PASAJES[id_destino][clase_destino] += cant_pasajes
    return True


def mostrar_cant_ventas():
    """
    Muestra la cantidad de boletos vendidos por destino y clase.s
    """
    print("CANTIDAD DE VENTAS POR DESTINO Y CLASE:")
    for k, v in DB_CANT_PASAJES.items():
        print(f"\n{DB_NOMBRES[k]}\n")
        for sub_v, price in v.items():
            print(f"- {sub_v}: {price}")


def programa_principal():
    """
    Ejecuta el programa.
    """
    while True:
        opcion_usuario = menu_principal()
        if opcion_usuario == 2:
            print("\nRESUMEN SESION:\n")
            mostrar_cant_ventas()
            print(f"\nGANANCIAS TOTALES: ${sum(RECAUDOS)}")
            input("\nPresione ENTER para salir...")
            break

        else:
            datos_destino_usuario = datos()
            valor_pasaje_usuario = valor_pasaje(datos_destino_usuario)
            print(f"\nValor del pasaje: ${valor_pasaje_usuario}")
            while True:
                try:
                    cant_pasajes_usuario = int(
                        input("\nCantidad de pasajes a comprar: "))
                    break
                except ValueError:
                    print("Ingrese solo numeros enteros, por favor.")
            tipo_descuento_usuario = descuento(cant_pasajes_usuario)
            if not tipo_descuento_usuario == 0.0:
                print(
                    f"\nAplica para descuento del {tipo_descuento_usuario*100}% del total de la compra.")
            pago_total_usuario = pago(
                cant_pasajes_usuario, valor_pasaje_usuario, tipo_descuento_usuario)
            print(f"\nTotal a pagar: ${pago_total_usuario}")

            while True:
                check_compra = input("\nConfirmar la compra (S/N): ").upper()
                if check_compra in ("S", "N"):
                    break
                print("Opcion no valida, intente denuevo.")

            if check_compra == "S":
                registrar_venta(datos_destino_usuario, cant_pasajes_usuario)
                RECAUDOS.append(pago_total_usuario)
                print("\nCompra realizada con exito.")
                print("\nVolviendo al menu principal...\n")

            else:
                print("\nHa cancelado la compra.\n")


if __name__ == "__main__":
    programa_principal()
