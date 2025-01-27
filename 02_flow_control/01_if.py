###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar un bloque de código si se cumple una condición.
###

import os

os.system("clear")

edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


nota = 10

### Ojo, en cuanto cumple la primera ya no revisa las demás
if nota > 9:
    print("Excelente")
elif nota > 7:
    print("Sobresaliente")
else:
    print("Aprobado")


carne = True
mayor_edad = True

if carne and mayor_edad:
    print("Puedes conducir")