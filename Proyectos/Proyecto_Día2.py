#Hacer un programa que pregunte el nombre y cuanto ha vendido este mes (suponiendo que las comisiones son del 13%

nombre= input("Hola, ¿cual es tu nombre? ")
venta= int(input("¿Cuanto haz vendido este mes? "))
comision=round(venta * 13 / 100,2)
print(f"Hola {nombre}, este mes has conseguido ${comision} en comisiones !sigue así¡")