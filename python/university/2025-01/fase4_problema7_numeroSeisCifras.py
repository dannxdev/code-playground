import os

# Limpia la consola en cada ejecucion.
os.system('cls')


def validar_numero(numero: int):
    """
    Que recibe como parámetro el número y determina si el 
    número es de 6 dígitos, si es de 6 dígitos retorna True 
    de lo contrario retorna False.
    """

    # Validando si el numero ingresado es entero:
    if isinstance(numero, int):
        if len(str(numero)) == 6 and numero > 0:
            # Si el numero contiene 6 digitos y es positivo:
            return True
    return False


def descomponer_numero(numero: int):
    """
    Descomponga un número N de 6 dígitos en tres números de 
    dos dígitos cada uno. Ejemplo: N=121536 -> a=12 b=15 c=36 
    """

    # Creando la lista que almacenara los numeros separados
    nums_dos_digitos = []
    num = ""  # almacenara los numeros de 2 cifras

    # Itera cada digito del numero ingresado como cadena:
    for digito in str(numero):
        num += digito
        if len(num) == 2:
            # Si la string num ya contiene 2 numeros se agrega el numero
            # a la lista y se vacia la variable.
            nums_dos_digitos.append(num)
            num = ""

    # Retorna un diccionario {a: num1, b: num2, c: num3}
    return dict(zip("abc", nums_dos_digitos))


def calcular_tabla(a, b):
    """
    recibe los números a y b y genera la tabla de multiplicar 
    de a hasta b, donde a debe ser menor que b. 
    """

    print(f"- Tabla de multiplicar de a = {a} hasta b = {b}:\n")

    # Convierte los argumentos a y b a entros:
    a, b = int(a), int(b)
    if a < b:
        # Si a es menor que b:
        for m in range(a, b + 1):
            # Generando la tabla de multiplicar:
            for n in range(1, 11):
                print(f"{m} x {n} = {m * n}", end=", ")
            print("")

    else:
        print("  No se puede mostrar la tabla porque a >= b.")


def unir(a: int, c: int):
    """
    recibe a y c y debe retornar un solo número resultado de 
    unir a y c el número devuelto debe quedar de 4 cifras 
    Ejemplo: a=12 c=36 número queda =1236 
    """

    # Une lso valores de a y c, que son strings (temporalmente) y los convierte a entero.
    return int(a + c)


def principal():
    """
    Programa principal.
    """

    # Crando un bucle hasta que el numero del usuario sea valido:
    while True:
        try:
            numero_usuario = int(input("Ingrese un numero de 6 digitos: "))
            if validar_numero(numero_usuario):
                break
            print("Error: El numero debe tener 6 digitos.\n")
        except ValueError:
            print("Error: Ingrese solo numeros por favor.\n")

    print(f"\n- Numero Ingresado: {numero_usuario}\n")

    # Ejecutando cada una de las funciones y mostrando en pantalla el
    numeros_separados = descomponer_numero(numero_usuario)
    print(f"- Numero Descompuesto: {numeros_separados}\n")
    num_a = numeros_separados["a"]
    num_b = numeros_separados["b"]
    num_c = numeros_separados["c"]
    calcular_tabla(num_a, num_b)
    print(f"\n- Union a = {num_a} y c = {num_c}: {unir(num_a, num_c)}\n")


if __name__ == "__main__":
    print("========================================")
    print("      Problema 7: Numero de 6 digitos.      ")
    print("========================================\n")
    principal()

    input("\nPresione ENTER para salir.\n")
