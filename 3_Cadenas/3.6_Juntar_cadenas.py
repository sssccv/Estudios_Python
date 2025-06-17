# Existen varias formas de formar las cadenas, existe:

# f-string sirve para darle formato a las cadenas, se recomienda por ser más sencillo de escribir, más rápido y más legible
# su formato es VARIABLE=f"texto1{variable}"
num = 2
num2 = 3
resultado =f"el número es {num}"
print(resultado) # Esto es un ejemplo de como se usa el f-string
print()

# También existe el metodo format el cual es muy versatil, poderoso y permite form,ar cadenas más complejas
# Se escribe como Variable="texto1 {}".format(variable)
# Mientras adentro de las "" hayan {} se podrán meter una infinidad de variables con este formato, solo que es importante ponerlas en orden

resultado2= "{} y {} no son iguales".format(num,num2)
print(resultado2)# Esto es un ejemplo de como se usa el .format()
print()

nombre ="Rodrigo"
edad = 20

mensaje1 = f"el es {nombre} y tiene {edad} años" # Aquí fue hecho con fstring
mensaje2 = "el es {} y tiene {} años".format(nombre,edad) # Aqui fue hecho con .format

print(mensaje1)# Aquí fue hecho con fstring
print()

print(mensaje2)# Aqui fue hecho con .format
