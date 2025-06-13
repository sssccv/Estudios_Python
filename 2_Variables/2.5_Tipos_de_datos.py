# Python es un lenguaje de tipado dinámico, por lo que NO hay necesidad de indicar el tipo de variable al momento de declararla
# Los valores que pueden almacenar las variables son de distintos tipos , como:

# Numeros (INT): numeros enteros sin punto decimal (10, 309, -57)
numero_entero=12
print("numero entero es:",numero_entero, "y es ",type(numero_entero))

# Numeros con punto flotante (FLOAT): 3.1416 , -0.004
numero_con_punto=3.1416
print("numero con punto es:",numero_con_punto, "y es ",type(numero_con_punto))

# Cadenas de texto (STR): secuencias de caracteres (hola mundo)
cadena_de_texto="hola mundo"
print("la cadena de texto dice:",cadena_de_texto, "y es de tipo",type(cadena_de_texto))

# Booleanos (BOOL): valor lógico de verdadero (True) o falso (False), siempre tienen que empezar con mayuscula, estos valores los usaremos para controlar el flujo de los programas
booleano= True
print("el booleano es:",booleano, "y es de tipo",type(booleano))

# None: Tipo especial de Python que indica ausencia de valor
nada= None
print("nada es:",nada, "y es de tipo", type(nada))
