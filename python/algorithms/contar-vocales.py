# Contador de vocales en una frase

# Paso 1: Solicitar la frase al usuario
frase = input("Ingrese una frase: ").lower()  # Convertimos todo a minúsculas

# Paso 2: Inicializar un diccionario para contar vocales
vocales = {'a': 0, 'á': 0, 'e': 0, 'é': 0, 'i': 0,
           'í': 0, 'o': 0, 'ó': 0, 'u': 0, 'ú': 0, 'ü': 0}

# Paso 3: Recorrer cada carácter de la frase
for letra in frase:
    if letra in vocales:
        vocales[letra] += 1  # Incrementamos el contador si es vocal

# Paso 4: Calcular el total de vocales
total = sum(vocales.values())

# Paso 5: Mostrar resultados con formato
print(f"\nEstadísticas de vocales:")
print(
    f"a: {vocales['a']} | e: {vocales['e']} | i: {vocales['i']} | o: {vocales['o']} | u: {vocales['u']}")
print(f"Total de vocales: {total}")
