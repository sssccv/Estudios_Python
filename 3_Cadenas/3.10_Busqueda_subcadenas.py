# El metodo find() devuelve el índice de la primera aparición de una subcadena dentro de una cadena.
# Si no encuentra la subcadena, devuelve -1.

cadena = "Hola mundo" # Definimos una cadena de texto
posicion = cadena.find("mundo") # Buscamos la posición de la subcadena "mundo" dentro de la cadena
print(posicion)
print()


cadena2 = "hola a todos, me llamo Juan y tengo 12" # Definimos una segunda cadena de texto
subcadena = cadena2[30:36] # Extraemos una subcadena desde la posición 30 hasta la 35 (el índice 36 no se incluye)
print(subcadena) # Mostramos la subcadena extraída
posicion2 = cadena2.find(subcadena) # Buscamos la posición de esa subcadena dentro de la cadena original

print(f"El índice de la cadena '{subcadena}' es {posicion2}")
