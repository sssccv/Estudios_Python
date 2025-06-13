import math

print("*** constantes en Python ***")

PI = 3.14159
print("El valor de PI es:",PI)
print()

NOMBRE_BASE_DATOS = "clientes_db"
print("Nombre de la base de datos:",NOMBRE_BASE_DATOS)
print()

# Esto NO se debe hacer, no se debe modificar el valor de una constante aunque python lo permita
NOMBRE_BASE_DATOS = "listado_clientes_db"
print("NO cambiar el valor de una constante:",NOMBRE_BASE_DATOS)
print()

# Usar una constante del lenguaje Python, aunque en este caso no está en mayusculas
print("Valor de math.pi", math.pi)