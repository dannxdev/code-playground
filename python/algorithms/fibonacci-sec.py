def fibonacci_seq(start, end):
    """Recibe dos valores enteros o flotantes, uno de inicio 
    donde empieza la secuencia y otro que determina donde finaliza."""

    sequence = []  # lista vacia que recibira la secuencia resultante del bucle while
    fib = 0
    if start == 0:
        a = 0
        b = 1
    else:
        a = start
        b = start + 1

    # anade los valores que inicializan la secuencia, dependen del valor start dado como argumento:
    sequence.append(a)
    sequence.append(b)

    # bucle que aplica la logica de fibonacci
    while fib < end:
        fib = a + b
        sequence.append(fib)
        a = b
        b = fib

    del sequence[-1]

    return sequence  # retorna una lista con la secuencia


test = fibonacci_seq(0, 100)
print(test)
