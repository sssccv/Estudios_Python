# Crear un sistema de reserva de Hoteles que contenga: nombre del cliente, Dias de estancia, Tarifa diaria, indicar si el cuarto tiene vista al mar
# Mandamos a imprimirlo
# Hacemos unos cambios despues y lo mandamos a re-imprimir

# Primera definicion de variables
nombre_cliente = "Sergio Salazar"
dias_estancia = 4
tarifa_diaria = 140.50
Vista_al_mar = False

# Primera impresión
print()
print("Primera impresion")
print("*** Sistema de Reserva de Hoteles ***")
print("Cliente:",nombre_cliente)
print("Días de estancia:", dias_estancia)
print("Tarifa diaria:",tarifa_diaria)
print("Habitación con vista al mar?",Vista_al_mar)
print("Su total sería de",(dias_estancia*tarifa_diaria),"$")

# Segunda definicion de variables
nombre_cliente = "Sergio Salazar"
dias_estancia = 7
tarifa_diaria = 160.75
Vista_al_mar = True

# Segunda impresión
print()
print("Segunda impresion")
print("*** Sistema de Reserva de Hoteles ***")
print("Cliente:",nombre_cliente)
print("Días de estancia:", dias_estancia)
print("Tarifa diaria:",tarifa_diaria)
print("Habitación con vista al mar?",Vista_al_mar)
print("Su total sería de",(dias_estancia*tarifa_diaria),"$")