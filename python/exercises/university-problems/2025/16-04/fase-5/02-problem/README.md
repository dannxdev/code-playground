# Problema 2: Sistema de Control de Inventario de Libros - Biblioteca Universitaria

## Enunciado

Una biblioteca universitaria requiere un programa en Python para gestionar el control de su inventario de libros. Cada libro pertenece a una categoría específica y tiene un costo fijo según su categoría.

### Tabla de Precios por Categoría (Precios Constantes)

| Categoría    | Precio por libro |
|--------------|------------------|
| Ciencia      | $80.000          |
| Literatura   | $50.          |
| Tecnología   | $100.         |
| Historia     | $60.          |

**Nota:** Estos precios son de referencia y no cambian durante la ejecución del programa.  
**Fuente:** Autor.

## Requisitos Funcionales del Programa

El programa debe permitir:

1. Definir la cantidad total de libros a registrar (`N`), ingresada por el usuario.
2. Para cada uno de los `N` libros, solicitar:
   - Categoría del libro (Ciencia, Literatura, Tecnología o Historia).
   - Cantidad de unidades de ese libro que ingresan al inventario.
3. Al finalizar el registro, mostrar en pantalla:
   - Número total de libros (unidades) en el inventario.
   - Valor total del inventario sin descuentos.
   - Valor promedio por libro en el inventario.
   - Cantidad de unidades registradas en cada una categoría.

## Requisitos Técnicos Obligatorios

- Utilizar **constantes** para almacenar los precios de cada categoría.
- Emplear **estructuras cíclicas** (bucles) para registrar los `N` libros.
- Implementar **funciones** separadas para calcular:
  - Total de unidades de libros en el inventario.
  - Valor total del inventario.
  - Valor promedio por libro.
  - Cantidad de unidades por cada categoría.
- Utilizar **listas (vectores)** para almacenar y manejar la cantidad de libros por categoría.