## 🏪 **Sistema de Gestión de una Tienda Online**

### **Descripción:**
Crea un sistema para gestionar una tienda online que maneje productos, clientes y pedidos.

### **Requisitos:**

#### **1. Clase `Producto`**
- Atributos: `id`, `nombre`, `precio`, `stock`
- Métodos: 
  - `mostrar_info()` - muestra la información del producto
  - `actualizar_stock(cantidad)` - actualiza el stock

#### **2. Clase `Cliente`**
- Atributos: `id`, `nombre`, `email`, `carrito_compras` (lista de productos)
- Métodos:
  - `agregar_al_carrito(producto, cantidad)`
  - `eliminar_del_carrito(producto)`
  - `ver_carrito()`
  - `realizar_compra()` - vacía el carrito y devuelve el total

#### **3. Clase `Pedido`**
- Atributos: `id_pedido`, `cliente`, `productos`, `total`, `fecha`
- Métodos:
  - `calcular_total()`
  - `mostrar_pedido()`

#### **4. Clase `Tienda`** (opcional - para gestión general)
- Atributos: `nombre`, `productos`, `clientes`, `pedidos`
- Métodos para gestionar inventario y ventas

### **Ejemplo de uso esperado:**
```python
# Crear productos
producto1 = Producto(1, "Laptop", 999.99, 10)
producto2 = Producto(2, "Mouse", 25.50, 50)

# Crear cliente
cliente = Cliente(1, "Ana García", "ana@email.com")

# Agregar productos al carrito
cliente.agregar_al_carrito(producto1, 1)
cliente.agregar_al_carrito(producto2, 2)

# Realizar compra
total = cliente.realizar_compra()
print(f"Total de la compra: ${total}")
```

### **Retos adicionales:**
- Manejar excepciones (stock insuficiente, producto no encontrado)
- Implementar descuentos
- Guardar historial de compras por cliente
- Búsqueda de productos

¿Te gustaría que te ayude con alguna parte específica o prefieres intentarlo por tu cuenta primero?