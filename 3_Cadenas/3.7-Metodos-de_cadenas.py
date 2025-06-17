# Las cadenas vienen con una serie de métodos que facilitan su uso

# Upper() -> cambia las letras a mayusculas
cadena1 = "Hola Mundo"
print(f"cadena original: {cadena1}")
mayusculas =cadena1.upper()
print(f"cadena en mayusculas: {mayusculas}")
print()

# lower() -> Cambia las letras a minúsculas
cadena2 = "HOLA MUNDO"
print("cadena original: {}".format(cadena2))
minusculas = cadena2.lower()
print("cadena en minúsculas: {}".format(minusculas))
print()

# strip() -> Quita espacios en blanco al inicio y al final de una cadena
cadena3 = " hola mundo "
print(f" esta es la cadena original: {cadena3} uwu")
strip = cadena3.strip()
print("esta es la cadena modificada: {} uwu".format(strip))
print()

# Otros ejemplos

texto1 = "Hola Mundo"
print(f"cadena original{texto1}")
mayusculas= texto1.upper() #En este paso se pasa el texto a mayusculas, pero se puede omitir y solo poner la variable.uper o lower al momento de formatearla
print("cadena modificada a mayusculas: {}".format(texto1))
print(f"Cadena modificada a minusculas: {texto1.lower()}") # Aqui la estamos convirtiendo a minuscula sin crear otra variable
print()

texto2= "   hola   "
print("el mensaje sin modificar era: {}".format(texto2))
print(f"el mensaje  (modificado) era: {texto2.strip()}")