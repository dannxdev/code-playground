import os
os.system("cls")


def sep():
    print("--------------------")


def tabla_multiplicar(num, large):
    """Recibe como argumentos dos valores int, el primer argumento representa de que numero queremos obtener su tabla
    y el segundo argumento hasta que numero queremos extender la tabla, generalmente inicia la tabla multiplicando por 0"""
    try:
        num = int(num)
        large = int(large)
        print(f'Generando tabla del {num} hasta el {large}...')
        sep()
        for i in range(large+1):
            print(f'{num} x {i} = {num*i}')
        sep()
    except ValueError:
        print("Error: Los argumentos a recibir deben ser numeros")


tabla_multiplicar(9, 10)

# output:

# Generando tabla del 9 hasta el 10...
# --------------------
# 9 x 0 = 0
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90
# --------------------
