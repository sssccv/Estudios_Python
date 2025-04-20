#casting = convertir un tipo de variable a otro
#coverción implicita= python lo hace automáticamente
num1 = 20
num2 = 30.5
num1= num1 + num2
print(type(num1))
print(type(num2))

#converción explícita= lo tenemos que hacer manualmente
num3=5.8
print(num3)
print(type(num3))

num4= int(num3)
print(num4)
print(type(num4))

edad=input("dime tu edad: ")


print(type(edad))
edad=int(edad)

print(type(edad))

nueva_edad=1+edad
print("tu nueva edad va a ser"+nueva_edad)



num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))