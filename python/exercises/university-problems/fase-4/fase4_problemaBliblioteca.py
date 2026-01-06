import os
os.system('cls')

DB_LIBROS = {
    1: {"TIPO": "General", "COSTO": 500, "PRESTAMOS": 0},
    2: {"TIPO": "Coleccion", "COSTO": 1000, "PRESTAMOS": 0},
    3: {"TIPO": "Reserva", "COSTO": 5000, "PRESTAMOS": 0}
}


def validar_codigo(codigo):
    """
    Recibe el codigo del libro y valida si cumple las codiciones.
    """

    codigo = str(codigo)

    if len(codigo) == 6:
        # Si la longitud del codigo es 6, separamos el codigo:
        primer_digito = int(codigo[0])
        tres_digitos = int(codigo[1] + codigo[2] + codigo[3])
        # Si el primer digito esta entre 1, 2 o 3, y los siguientes 3 en el rango 101-108:
        return primer_digito in (1, 2, 3) and 101 <= tres_digitos <= 108
    return False


def obtener_costo(codigo):
    """
    Obtiene el costo del libro.
    """

    primer_digito = int(str(codigo)[0])
    return DB_LIBROS[primer_digito]["COSTO"]


def registrar_prestamo(codigo):
    """
    Registra en la base de datos el prestamo del libro.
    """

    if validar_codigo(codigo):
        primer_digito = int(str(codigo)[0])
        tipo = DB_LIBROS[primer_digito]["TIPO"]
        DB_LIBROS[primer_digito]["PRESTAMOS"] += 1
        print(
            f"Prestamo libro tipo '{tipo}' registrado exitosamente. Costo devolucion ${obtener_costo(codigo)}")
        return True
    return False


def mostrar_ganancias():

    print("RECOLECCION:\n\n")

    total_ganancias = 0
    for identificador, datos in DB_LIBROS.items():
        total = datos["COSTO"] * datos["PRESTAMOS"]
        total_ganancias += total

        print(
            f"ID Libro: {identificador}\n- Tipo: {datos["TIPO"]}\n- Cant. Prestamos: {datos['PRESTAMOS']}\n- Costo: ${datos['COSTO']}\n- Total: ${total}")
        print("\n")

    print(f"Ganancia Total: ${total_ganancias}\n")


def principal():
    """
    Programa principal.
    """

    while True:
        print("BIBLIOTECA LEXUS\n\n1. Prestamo\n2. Recoleccion\n3. Salir\n")
        while True:
            try:
                opcion = int(input("Seleccione una opcion (1 - 3): "))
                if opcion in (1, 2, 3):
                    break

            except ValueError:
                print("Opcion no valida. Intentelo denuevo.")

        if opcion == 1:
            print("\nPRESTAMO LIBRO\n")
            while True:
                try:
                    codigo_libro = int(
                        input("Escriba el codigo del libro (6 digitos), para salir escriba 0: "))
                    if validar_codigo(codigo_libro):
                        registrar_prestamo(codigo_libro)
                        break
                    if codigo_libro == 0:
                        print("\n")
                        break
                except ValueError:
                    print('Codigo no valido. Intentelo denuevo')

        elif opcion == 2:
            mostrar_ganancias()

        else:
            print("Saliendo del programa...\n")
            break


if __name__ == "__main__":
    principal()
