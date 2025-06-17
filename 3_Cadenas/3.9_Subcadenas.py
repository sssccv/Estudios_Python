# Una subcadena es una parte de una cadena principal
# Para conseguir una subcadena se pone [inicio:final] despues de una cadena (en lugar de inicio y final ponemos el número que corresponde al caracter que queremos "recortar"

cadena = "Hola, Mundo!"
print(f"Esta es la cadena original: \'{cadena}\'")
print()

# Obtenemos la subcadena de hola [inicio:fin (sin incluirlo)]
subcadena_hola =cadena[0:4]
print(subcadena_hola)
print("La primera subcadena de: \'{}\' es: {}".format(cadena,subcadena_hola))
print()

# Conseguir la subcadena de mundo
subcadena_mundo = cadena[6:11]
print(subcadena_mundo)
print("La segunda subcadena de: \'{}\' es: {}".format(cadena,subcadena_mundo))
