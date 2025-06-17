# Reemplazar subcadenas (replace): El metodo .replace() reemplaza una subcadena por otra dentro de una cadena principal
cadena = "Hola mundo!"
print(f"la cadena original es: \'{cadena}\'")

# Sustituyo mundo por a todos
nueva_cadena= cadena.replace("mundo","a todos")
print("la cadena modificada es: \'{}\'".format(nueva_cadena))

# Prueba re sustituir hola por adios sin tener que crear una nueva variable
print(cadena.replace("Hola","Adios"))