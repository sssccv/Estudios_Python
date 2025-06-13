# Crear el detalle de un producto de una tienda

# El detalle tiene que tener: Nombre, precio, stock, si está disponible
#imprimimos esto

# Hacemos unos cambios y re imprimimos
# ----------------------------------------------------------------------------------------------------------------------
# Primera declaracion
nombre_producto = "zapatos Grandes"
precio_producto = 120.00
stock_producto  = 12
esta_disponible = True

# Primera impresion
print("***** Producto *****")
print("Nombre del producto:",nombre_producto)
print("Precio del producto: $",precio_producto)
print("Stock del producto:",stock_producto)
print("Hay stock?",esta_disponible)

# Segunda declaracion
nombre_producto = "zapatos Chicos"
precio_producto = 110.50
stock_producto  = 0
esta_disponible = False

# Segunda impresion
print()
print("***** Producto *****")
print("Nombre del producto:",nombre_producto)
print("Precio del producto: $",precio_producto)
print("Stock del producto:",stock_producto)
print("Hay stock?",esta_disponible)