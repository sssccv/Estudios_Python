# Una vez se crea una cadena, los caracteres dentro de ella no pueden ser modificados, si queremos modificar una cadena, entonces se tiene que crear una nueva cadena

cadena1 = "Hola mundo"
print(cadena1)
# Aqui la cadena1, siempre será "Hola mundo" hasta que se modifique el contenido

cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)
# Aquí la cadena1 ya ha sido modificada, pero se guardó antes el primer mensaje dentro de otra cadena