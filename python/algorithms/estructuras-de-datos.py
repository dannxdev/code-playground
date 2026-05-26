import os

os.system('cls')

# EJERCISIOS DE ESTRUCTURAS DE DATOS EN PYTHON
# Organizando un diccionario de tuplas:

# El siguiente codigo organiza una lista de tuplas, cada una con tres datos en un diccionario mas estructurado,
# util para escribir luego el diccionario en un archivo `.json`.

# (repartidor, fecha, cliente)
entregas = [
    ('Mario', '2025-07-01', 'ClienteA'),
    ('Mario', '2025-07-01', 'ClienteB'),
    ('Mario', '2025-07-02', 'ClienteC'),
    ('Mario', '2025-07-02', 'ClienteC'),
    ('Luisa', '2025-07-01', 'ClienteG'),
    ('Mario', '2025-07-02', 'ClienteC'),
    ('Mario', '2025-07-02', 'ClienteG'),
    ('Luisa', '2025-07-01', 'ClienteD'),
    ('Luisa', '2025-07-01', 'ClienteE'),
    ('Luisa', '2025-07-02', 'ClienteF'),
    ('Mario', '2025-07-01', 'ClienteA')  # Entrega repetida
]

resultado = {}
# recorre cada tupla en de la lista entregas
for tupla in entregas:
    # Siempre que la tupla tenga 3 datos, los separa en tres variables:
    nombre, fecha, cliente = tupla

    if nombre not in resultado:
        # agrega el nombre como clave principal al diccionario:
        resultado[nombre] = {}

    if fecha not in resultado[nombre]:
        # agrega un diccionario como value de la clave principal y nade en este sub-diccionario
        # el segundo valor como key, en la que el value es una lista vacia:
        resultado[nombre][fecha] = []

    if cliente not in resultado[nombre][fecha]:
        # Finalmente anade el 3 dato de la tupla a la lista, value del sub-diccionario:
        resultado[nombre][fecha].append(cliente)

print(resultado)
