#format en lugar de escribir mucho texto pones {} en donde va una variable y luego de los "" pones .format(variables) por ejemplo:

color_auto="rojo"
matricula=65476
print("Mi auto es {} y de matrícula {}\n".format(color_auto,matricula))

#cadena literal agregas una f antes de las "" en el print, agregas las {} pero ahora con el nombre de la variable adentro

print(f"mi auto es {color_auto} y tiene matrícula {matricula}\n")

x = 10
y = 5

print("mis números son " + str(x) + " y " + str(y) ) #Esto no es práctico
print("-------------------")
print("mis números son {} y {} \nAquí está en .format\n".format(x,y))
print(f"mis números son {x} y {y} \nAquí está como cadena literal\n")

print("la suma de {} y {} es igual a {}".format(x,y,x+y))

color = "rojo"
matricula2=54926
print(f"el auto es de color {color} y tiene matrícula {matricula2}")

puntos_anteriores = 875
puntos_nuevos = 350

print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_nuevos+puntos_anteriores))