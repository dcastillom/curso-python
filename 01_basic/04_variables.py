###
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
# Hay una guía de estilos de Python
###

# Asignación de variables
# No hace falta declarar el tipo de variable
my_name = "Daniel"
print(my_name)
my_name = "Daniel 2"
print(my_name)

# Tipado dinámico
# El tipo de dato se determina en tiempo de ejecución
my_name = 1
print(type(my_name))
my_name = "Daniel"
print(type(my_name))


# Tipado fuerte
# No se pueden mezclar tipos de datos
# print("Hola" + 2) # Error
age = 10
print("Hola " + str(age))
print(f"Hola, {my_name}. Tienes {age} años")

# No recomendado, pero posible
name, age = "Daniel", 10

# Convenciones de nombres de variables
mi_nombre = "Daniel" # snake_case
mi_nombre_123 = "Daniel" # snake_case con números
MI_CONSTANTE = "Valor" # Todas las letras en mayúsculas para constantes

# Palabras reservadas
# and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal,
# not, or, pass, raise, return, True, try, while, with, yield


# Anotación de tipos
# Lo marco como bool pero luego se puede cambiar a otro tipo
is_active: bool = True # Anotación de tipo
print(is_active)
is_active = 3
print(is_active)
print(type(is_active))

