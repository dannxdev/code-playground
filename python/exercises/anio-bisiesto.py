import os

# Borrando el contenido de la consla en cada ejecucion:
os.system('cls')

# Calculator Año Bisiesto
# Creando la funcion que calcula si un año es bisiesto:


def is_year_leap(year):
    # Si year es divisible por 4 pero no por 100,
    # o es divisible entre 400: es bisiesto.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Buscador cantidad de dias
# Se crea un funcion que devuelve el numero de dias que tuvo un año, incluyendo si este es bisiesto.
def days_in_month(year, month):
    if month > 12 or year < 1582:
        return None
    else:
        day_months = {30: [4, 6, 9, 11], 31: [1, 3, 5, 7, 8, 10, 12]}
        if month != 2:
            for k, v in day_months.items():
                if month in v:
                    return k
        else:
            if is_year_leap(year):
                return 29
            return 28


def day_of_year(year, month, day):
    if month < 3:
        month += 12  # Convierte enero (1) a 13 y febrero (2) a 14
        year -= 1    # Resta 1 al año para tratar enero y febrero como parte del año anterior

    # Asignar variables según la fórmula de Zeller
    q = day
    m = month
    k = year % 100
    j = year // 100

    h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7

    # Retorna el día de la semana (0 = sábado, 1 = domingo, ..., 6 = viernes)
    return h
