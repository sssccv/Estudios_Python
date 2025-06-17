# Para separar una sola cadena en varias se usa la función (split), permite dividir una cadena en una lista de subcadenas

datos = "Jorge, 35, Panamá, Atún, Perro" # Aqui se meten los datos
lista= datos.split(",") # Aqui se separan los datos cada vez que en la variable datos haya una coma (si no ponemos el "," separará la cadena cada que haya un espacio en blanco)
print(lista) # Aqui imprimo la lista
print()

datos2 = "Hola mundo"
lista2 = datos2.split()
print(lista2)
print()

datos3 = "mi nombre es ezequiel y me gustan los peces"
lista3 = datos3.split("e") # Prueba separando la lista pero cada vez que haya una e
print(lista3)