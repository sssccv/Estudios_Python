# Crear un programa para generar un emaila partir de los siguientes datos

# Nombre : Sergio Salazar Ramírez
# Empreza : Bunny Studio
# Dominio: bun.mx
# email = sergio_salazar_ramirez@bunnystudio.bun.mx

# Variables originales
nombre = " Sergio Salazar Ramírez "
empreza = "Bunny Studio"
dominio = ".bun.mx"

# Normalizo y consigo los nombres por separado
nombre_remplazado=nombre.strip().replace(" ","_").lower()

#Normalizo y consigo el nombre de la empreza por separado y lo junto para el @
nombe_empreza=empreza.replace(" ","").lower()

# Normalizo el dominio
dominio_normalizado = "@"+nombe_empreza+dominio.strip()

# Consigo el correo ya completo
correo="{}{}".format(nombre_remplazado,dominio_normalizado)

#Hago el print del simulador
print("*** Generador de Email ***")
print(f"Nombre de usuario: {nombre}")
print(f"Nombre de usuario normalizado: {nombre_remplazado}")
print()
print("Nombre de la empreza: {}".format(empreza))
print("Extensión del dominio: {}".format(dominio))
print("Dominio de email normalizado: {}".format(dominio_normalizado))
print()
print(f"Email final denerado: {correo}")
