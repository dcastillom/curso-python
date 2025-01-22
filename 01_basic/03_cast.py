###
# 03 - Casting de tipos
# Transformar un tipo de dato a otro se llama casting.
###

print("Convesión de tipos:")
print(type("100"))
print(type(int("100")))
print(bool("100")) # True
print(bool(0)) # False
print(bool(-1)) # Ojo, -1 es True
print(int(2.5)) # Elimina la parte decimal, no redondea