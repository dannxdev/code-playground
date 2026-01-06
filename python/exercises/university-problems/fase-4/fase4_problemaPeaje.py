import os

os.system('cls')

nombre_vehiculos = {
    1: "Vehiculo",
    2: "Camion",
    3: "Tractomula"}

vehiculos_valor_peaje = {1: 3500, 2: 12000, 3: 16000}
contador_paso = {1: 0, 2: 0, 3: 0}
registro_pagos = {1: 0, 2: 0, 3: 0}


def validar_vehiculo(id_vehiculo):
    """
    AALLS
    """

    if id_vehiculo in nombre_vehiculos:
        return True
    return False


def valor_a_pagar(id_vehiculo):
    """
    Retorna el valor a pagar segun el ID del vehiculo ingresado.
    """
    return vehiculos_valor_peaje.get(id_vehiculo, None)


def registrar_paso(id_vehiculo):
    """
    Registra el paso de cada vehiculo y lo muestra en pantalla.
    """

    contador_paso[id_vehiculo] += 1
    print(
        f"Se registro: {nombre_vehiculos[id_vehiculo]}, 1 Paso, Valor: ${vehiculos_valor_peaje[id_vehiculo]}.")
    return True


def total_por_vehiculo(id_vehiculo):
    """
    Pero definir
    """
    return vehiculos_valor_peaje[id_vehiculo] * contador_paso[id_vehiculo]


def suma_total_diario():
    """
    Suma todos las ganacias para todos los vehiculos.
    """
    return sum(registro_pagos.values())


def mostrar_resumen_final():
    """
    Muestra todos los resultados que pide el problema
    """
    print("\n" + "="*50)
    print("RESUMEN DEL DÍA")
    print("="*50)

    # Total recaudado por cada tipo
    for tipo_id in [1, 2, 3]:
        print(
            f"{nombre_vehiculos[tipo_id]}: {contador_paso[tipo_id]} vehículos - ${registro_pagos[tipo_id]:,}")

    # Total general
    print(f"\nTOTAL RECAUDADO: ${suma_total_diario():,}")

    # Tipo que más transita
    # key trae la clave a la que corrsponde el valor maximo, no el valor maximo.
    tipo_mas_transitado = max(
        contador_paso, key=contador_paso.get)  # type: ignore
    print(
        f"Tipo que más transita: {nombre_vehiculos[tipo_mas_transitado]} ({contador_paso[tipo_mas_transitado]} vehículos)")


def principal_sistema_peajes():
    """
    Ejecuta el programa.
    """
    print("Sistema de peajes - Ingrese 0 para finalizar el día")

    while True:
        try:
            id_paso = int(
                input("Escriba el ID del vehiculo (1,2,3) o 0 para terminar: "))

            # Verificar si es la señal de fin
            if id_paso == 0:
                break

            if validar_vehiculo(id_paso):
                registrar_paso(id_paso)
                pago = valor_a_pagar(id_paso)
                registro_pagos[id_paso] += pago  # type: ignore
                print("Registro exitoso.\n")
            else:
                print("ID no válido. Use 1, 2 o 3.\n")

        except ValueError:
            print("Ingrese solo números por favor.\n")

    mostrar_resumen_final()


if __name__ == "__main__":
    principal_sistema_peajes()
