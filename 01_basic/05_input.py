###
# 05 - Entrada de usuario
# La función input() permite al usuario introducir datos a través de la consola.
###


nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}")

age = input("Introduce tu edad: ")
# Todo lo que venga de input será un string
# print(f"Dentro de dos años tendrças {age + 2} años") # Error, age es un string
print(f"Dentro de dos años tendrças {int(age) + 2} años") # Casting de tipow

# Se pueden obtener varios valores a la vez
country, city = input("Introduce tu país y ciudad: ").split()
print(f"Vives en {country}, {city}")