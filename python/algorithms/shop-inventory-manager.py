import json
import re

# -------------------------------
# Clase para representar un producto
# -------------------------------


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        """
        Inicializa un producto con código, nombre, precio y stock.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """
        Devuelve una representación legible del producto.
        """
        return f'CODIGO: {self.codigo}, NOMBRE: {self.nombre}, PRECIO: {self.precio}, STOCK: {self.stock}'

    def act_stock(self, cantidad):
        """
        Actualiza el stock del producto.
        Args:
            cantidad (int): Cantidad a sumar (positiva) o restar (negativa).
        Returns:
            bool or None: True si la operación es válida, False si no hay suficiente stock, None si cantidad es 0.
        """
        if cantidad > 0:
            self.stock += cantidad
            return True
        elif cantidad < 0:
            if self.stock + cantidad >= 0:
                self.stock += cantidad
                return True
            return False
        return None

    def es_caro(self):
        """
        Determina si el producto es considerado caro.
        Returns:
            bool: True si el precio es mayor a 100000.
        """
        return self.precio > 100000


# -------------------------------
# Funciones auxiliares
# -------------------------------

def validar_codigo(code):
    """
    Valida que el código comience con una letra seguida de números.
    Args:
        code (str): Código a validar.
    Returns:
        str or None: Código en mayúsculas si es válido, None si no lo es.
    """
    if re.match(r'^[a-zA-Z]{1}\d+$', code):
        return code.upper()
    return None


def agregar_producto(inventario):
    """
    Solicita datos al usuario y agrega un nuevo producto al inventario.
    Args:
        inventario (dict): Diccionario que almacena los productos.
    """
    print('AGREGAR UN NUEVO PRODUCTO')
    while True:
        codigo = input('Código: ')
        codigo = validar_codigo(codigo)
        if codigo and codigo not in inventario:
            break
        print('Ese código ya existe o es inválido, ingrese uno diferente.')

    nombre = input('Nombre: ')

    while True:
        try:
            precio = float(input('Precio: '))
            if precio >= 0:
                break
            print('El precio no puede ser negativo.')
        except ValueError:
            print('Ingresa solo números por favor.')

    while True:
        try:
            stock = int(input('Stock: '))
            if stock >= 0:
                break
            print('El stock no puede ser negativo.')
        except ValueError:
            print('Ingresa solo números enteros por favor.')

    nuevo_producto = Producto(codigo, nombre, precio, stock)
    inventario[codigo] = nuevo_producto
    print('El producto ha sido agregado exitosamente.')


def mostrar_productos(inventario):
    """
    Muestra todos los productos del inventario.
    """
    print('LISTA DE PRODUCTOS:')
    if not inventario:
        print('Inventario vacío.')
    else:
        for producto in inventario.values():
            print(f'- {producto}')
        print(f'Total de productos: {len(inventario)}')


def buscar_por_codigo(inventario, codigo):
    """
    Busca un producto por su código.
    Args:
        inventario (dict): Diccionario de productos.
        codigo (str): Código a buscar.
    Returns:
        Producto or None: El producto si se encuentra, None si no.
    """
    producto = inventario.get(codigo)
    if producto:
        print(producto)
        return producto
    return None


def realizar_venta(producto, cantidad):
    """
    Realiza una venta restando stock.
    Args:
        producto (Producto): Producto a vender.
        cantidad (int): Cantidad a vender.
    """
    if producto and cantidad > 0:
        if producto.act_stock(-cantidad):
            # Si producto == True & Cantidad > 0
            print('Venta realizada con éxito.')
        else:
            print('No hay suficiente stock para realizar la venta.')
    else:
        print('Cantidad inválida o producto no encontrado.')


def productos_caros(inventario):
    """
    Muestra los productos cuyo precio es mayor a 100000.
    """
    print('PRODUCTOS CAROS:')
    caros = [p for p in inventario.values() if p.es_caro()]
    if not caros:
        print('No hay productos caros en el inventario.')
    else:
        for producto in caros:
            print(f'- {producto}')
        print(f'Total de productos caros: {len(caros)}')


def guardar_inventario(inventario):
    """
    Guarda el inventario en un archivo JSON.
    """
    with open('inventario.json', 'w') as f:
        json.dump([
            {'codigo': p.codigo, 'nombre': p.nombre,
                'precio': p.precio, 'stock': p.stock}
            for p in inventario.values()
        ], f, indent=4)
    print('Inventario guardado en inventario.json.')


def cargar_inventario():
    """
    Carga el inventario desde un archivo JSON.
    Returns:
        dict: Inventario cargado.
    """
    try:
        with open('inventario.json', 'r') as f:
            datos = json.load(f)
            inventario = {}
            for item in datos:
                producto = Producto(
                    item['codigo'], item['nombre'], item['precio'], item['stock'])
                inventario[item['codigo']] = producto
            return inventario
    except FileNotFoundError:
        return {}


# -------------------------------
# Programa principal
# -------------------------------

def main():
    inventario = cargar_inventario()

    # Si no hay productos cargados, se agregan algunos de prueba
    if not inventario:
        productos_prueba = [
            Producto("P101", "Laptop HP", 120000, 10),
            Producto("P102", "Teclado mecánico", 150000, 25),
            Producto("P103", "Mouse inalámbrico", 35000, 30),
            Producto("P104", "Monitor 24 pulgadas", 199000, 15),
            Producto("P105", "Impresora multifuncional", 150000, 8)
        ]
        for p in productos_prueba:
            inventario[p.codigo] = p

    print('- GESTIÓN DE INVENTARIO EN PYTHON by Danny -')
    while True:
        start = input('¿Arrancar el programa? (S/N): ').upper()
        if start == 'S':
            while True:
                print(
                    '\nMENU PRINCIPAL:\n'
                    '1. Agregar nuevo producto\n'
                    '2. Mostrar todos los productos\n'
                    '3. Buscar producto por código\n'
                    '4. Realizar venta\n'
                    '5. Mostrar productos caros\n'
                    '6. Guardar y salir\n'
                )
                try:
                    opcion = int(input('Escoge una opción (1-6): '))
                except ValueError:
                    print('Ingresa solo una opción válida (1-6).')
                    continue

                if opcion == 1:
                    agregar_producto(inventario)
                elif opcion == 2:
                    mostrar_productos(inventario)
                elif opcion == 3:
                    codigo = input('Código: ')
                    codigo = validar_codigo(codigo)
                    if codigo:
                        if not buscar_por_codigo(inventario, codigo):
                            print('Producto no encontrado.')
                    else:
                        print('Código inválido.')
                elif opcion == 4:
                    codigo = input('Código del producto a vender: ')
                    codigo = validar_codigo(codigo)
                    if codigo:
                        producto = buscar_por_codigo(inventario, codigo)
                        if producto:
                            try:
                                cantidad = int(input('Cantidad a vender: '))
                                realizar_venta(producto, cantidad)
                            except ValueError:
                                print('Ingresa solo números enteros.')
                        else:
                            print('Producto no encontrado.')
                    else:
                        print('Código inválido.')
                elif opcion == 5:
                    productos_caros(inventario)
                elif opcion == 6:
                    guardar_inventario(inventario)
                    print('Saliendo del programa...')
                    break
                else:
                    print('Opción inválida.')
        elif start == 'N':
            print('Saliendo sin guardar...')
            break
        else:
            print('Por favor, ingresa S o N.')


# -------------------------------
# Punto de entrada del programa
# -------------------------------

if __name__ == '__main__':
    main()
