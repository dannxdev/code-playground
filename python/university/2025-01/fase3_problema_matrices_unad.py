import os


def mostrar_registro(registros):
    """
    Muestra todos los atletas con su respectivo registro de tiempos.
    """
    for k, v in registros.items():
        print(f"- {k.capitalize()}: {v}")
    print("\n")


def atletas_cumplen_rango_tiempo(registro):
    """
    Valida si los tiempos de cada atleta cumplen con la condicion de
    no tener un tiempo que exceda los 10.4 seg. Retorna un diccionario con los
    atletas y sus tiempos que cumplen la condicion. Retorna 'None' si no encuentra ninguno.
    """

    # Creando un diccionario que almacenara los atletas que cumplen el rango de tiempo < 10.4 seg:
    cumplen_rango_tiempo = {}

    # Iterando cada atleta y sus tiempos del registro:
    for atleta, tiempos in registro.items():
        # Se asume inicialmente que el atleta cumple las condiciones:
        atleta_cumple = True
        # Se itera cada tiempo del atleta:
        for t in tiempos:
            if t > 10.4:
                # Si uno de sus tiempos es mayor a 10.4 seg el atleta no cumple:
                atleta_cumple = False
                # Se detiene la iteracion y continua con el siguiente atleta:
                break

        if atleta_cumple:
            # Si al final de la iteracion no se encontro un tiempo > 10.4, se agrega el atleta
            # y sus tiempos al diccionario con los atletas que cumplen:
            cumplen_rango_tiempo[atleta] = tiempos

    if len(cumplen_rango_tiempo) == 0:
        # Si el diccionario de atletas que cumplen esta vacio (Ningun atleta cumplio):
        return None
    # Si no esta vacio se retorna el diccionario:
    return cumplen_rango_tiempo


def calcular_mejor_registro_individual(registro: dict):
    """
    Recibe el diccionario resultado de la funcion atletas_cumplen_rango_tiempo(registro),
    luego obtiene el mejor tiempo de cada atleta, y elige cual de todos es mejor.
    """

    # Creando un diccionario con cada atleta y su mejor tiempo:
    atletas_con_mejor_tiempo = {atleta: min(tiempos)
                                for atleta, tiempos in registro.items()}

    # Creando u diccionario que almacenara los atletas con igual mejor tiempo:
    atleta_mejor_tiempo = {}

    # Iterando cada atleta y su mejor tiempo del diccionario mejor_tiempo_atletas:
    for atleta, tiempo in atletas_con_mejor_tiempo.items():
        if tiempo == min(atletas_con_mejor_tiempo.values()):
            # Si el tiempo del atleta es igual al mejor tiempo calculado
            # se anade al diccioanrio atletas_con_mejor_tiempo
            atleta_mejor_tiempo[atleta] = tiempo

    # Devuelve el diccionario con el o los atletas con mejor tiempo.
    return atleta_mejor_tiempo


def calcular_mejor_promedio(registro: dict):
    """
    Recibe el diccionario resultado de la funcion atletas_cumplen_rango_tiempo(registro),
    luego obtiene el mejor promedio de cada atleta, y elige cual de todos es mejor.
    """

    # Creando un diccionario con cada atleta y su promedio:
    atletas_promedio = {atleta: round(
        (sum(tiempos))/len(tiempos), 2) for atleta, tiempos in registro.items()}

    # Si hay mas de un atleta que cumple la condicion del rango de tiempo:
    if len(registro) > 1:
        atleta_mejor_promedio = {}

        # Iterando cada atleta y su promedio del registro:
        for atleta, promedio in atletas_promedio.items():
            # Si el promedio del atleta es igual al mejo promedio registrado (mas bajo de todos):
            if promedio == min(atletas_promedio.values()):
                # Se añade atleta con mejor promedio al diccionario atleta_mejor_promedio
                atleta_mejor_promedio[atleta] = promedio

    else:
        # Si solo hay uno significa que es el que mejor promedio tiene:
        atleta_mejor_promedio = atletas_promedio

    # Devuelve el diccionario con el o los atletas con mejor promedio.
    return atleta_mejor_promedio


def mostrar_resultados_seleccion(atletas_mejor_tiempo, atletas_mejor_promedio):
    """
    Muestra en consola los resultados de la seleccion.
    """

    print("ATLETA MEJOR TIEMPO:")

    if len(atletas_mejor_tiempo) > 1:
        print("Hay mas de un atleta con el mejor tiempo: ")

    # Itera el diccionario atletas_mejor_tiempo mostrando los valores en consola:
    for atleta, tiempo in atletas_mejor_tiempo.items():
        # Muestra nombre y mejor tiempo del atleta en pantalla:
        print(f"\n- Nombre: {atleta.capitalize()}\n- Tiempo: {tiempo}")

    print("\nATLETA MEJOR PROMEDIO:")

    if len(atletas_mejor_promedio) > 1:
        print("Hay mas de un atleta con el mejor promedio: ")

    # Itera el diccionario atletas_mejor_promedio mostrando los valores en consola:
    for atleta, promedio in atletas_mejor_promedio.items():
        # Validando si el atleta con mejor promedio tiene tambien el mejor tiempo:
        if atleta in atletas_mejor_tiempo:
            # Muestra nombre y mejor promedio del atleta en pantalla:
            print("El atleta con mejor promedio ya esta convocado:")
        print(f"\n- Nombre: {atleta.capitalize()}\n- Promedio: {promedio}")


if __name__ == "__main__":
    os.system('cls')
    print("SOLUCION PROBLEMA DE MATRICES\n")
    print("\n== PROBLEMA 1: CLASIFICACION LIGA DE ATLETISMO CORRIENDO LIGERO ==")

    print("\n1. Realizar el registro manual.\n2. Usar un registro de prueba.")
    opcion_usuario = input("\nSelecciona una opcion (1 - 2): ")

    if opcion_usuario == "1":
        print("\nRegistrar tiempos manualmente.")
        registro_tiempos = {"juan": [], "carlos": [],
                            "pedro": [], "roberto": [], "raul": [], "david": []}

        for nombre_atleta, lista_tiempos in registro_tiempos.items():
            print(f"\nATLETA: {nombre_atleta.capitalize()}\n")

            for num_carrera in range(1, 7):
                tiempo_registrado = input(
                    f"- Tiempo (seg) Carrera N°{num_carrera}: ")
                while True:
                    try:
                        # Conviertiendo el numero en decimal:
                        tiempo_registrado = float(tiempo_registrado)
                        if 10.1 <= tiempo_registrado <= 10.5:
                            # Si el tiempo registrado esta entre 10.1 y 10.5 se agrega
                            # al registro y se detiene el bucle:
                            lista_tiempos.append(tiempo_registrado)
                            break

                        # Si el tiempo esta fuera del rango se vuelve a pedir un valor al usuario.
                        print(
                            "Advertencia: El tiempo excede el rango establecido (10.1 - 10.5).")
                        tiempo_registrado = input(
                            f"- Tiempo (seg) Carrera N°{num_carrera}: ")

                    # Si el usuario no ingreso un numero:
                    except ValueError:
                        print("Advertencia: Ingresa solo numeros por favor.")
                        tiempo_registrado = input(
                            f"- Tiempo (seg) Carrera N°{num_carrera}: ")

    else:
        print("\nUsando un registro de prueba.")

        # Diccionario con registro de tiempos predefinido, de prueba.
        registro_tiempos = {
            'juan': [10.34, 10.35, 10.41, 10.35, 10.14, 10.24],
            'carlos': [10.24, 10.17, 10.21, 10.36, 10.12, 10.34],
            'pedro': [10.14, 10.21, 10.38, 10.25, 10.11, 10.39],
            'roberto': [10.38, 10.19, 10.14, 10.26, 10.17, 10.4],
            'raul': [10.11, 10.3, 10.31, 10.14, 10.4, 10.41],
            'david': [10.34, 10.23, 10.35, 10.27, 10.48, 10.35]
        }

    print("\n-- RESULTADOS SELECCION ATLETAS --")

    print("\nAtletas Evaluados:\n")

    # Mostrando todos los atletas con sus tiempos:
    mostrar_registro(registro_tiempos)

    # Ejecutando la funcion que valida si los atletas cumplen el rango de tiempo:
    atletas_que_cumplen = atletas_cumplen_rango_tiempo(registro_tiempos)

    if atletas_que_cumplen is not None:
        # Si el diccionario de atletas que cumplen no esta vacio:
        # Calculando el mejor registro individual.
        resultados_mejor_tiempo = calcular_mejor_registro_individual(
            atletas_que_cumplen)

        # Calculando el atleta con mejor promedio.
        resultados_mejor_promedio = calcular_mejor_promedio(
            atletas_que_cumplen)

        # Mostrando los resultados en pantalla:
        mostrar_resultados_seleccion(
            resultados_mejor_tiempo, resultados_mejor_promedio)

    else:
        print(
            "NINGUN ATLETA TIENE UN TIEMPO MENOR AL RANGO ESTABLECIDO (< 10.4 SEG).")

    # Input al final evita que la cosola se cierre instantaneamente
    # y se puedan vizualizar los resultados.
    input("\nPresione ENTER para salir...")
