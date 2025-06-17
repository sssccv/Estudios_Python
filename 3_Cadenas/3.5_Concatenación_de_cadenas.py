# Concatenar: unir o enlazar una cosa con otra, generalmente cadenas de texto o elementos relacionados
# La concatenación de cadenas es una operación que permite combinar dos o mas cadenas para formar una nueva cadena
# Existen varias formas para concatenar cadenas

cadena1 ="Hola"
cadena2 = "Mundo"
concatenación = cadena1 +" "+ cadena2

# El operador "+" lo pones entre 2 cadenas y realiza la concatenación
print(concatenación) # Así es con una variable creada usando +
print(cadena1 +" "+ cadena2) # Asi es solo poniendo el +
print()

# La función "join" nos permite juntar tantas cadenas como querramos
concatenacion_join = ''.join([cadena1," ",cadena2])
print(concatenacion_join)