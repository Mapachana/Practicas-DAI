# Validacion de cadenas de [ ]
import random

n = 10
vec = [random.randint(0,2) for i in range(0,n)]

for i in range(0,n):
    if vec[i] == 0:
        vec[i] = "["
    else:
        vec[i] = "]"

print(vec)

contador = 0
valido = True
for i in range(0,n):
    if vec[i] == "[":
        contador = contador + 1
    else:
        contador = contador -1
    
    if contador < 0:
        valido = False

if contador > 0:
    valido = False

if valido:
    print("La cadena es valida")
else:
    print("La cadena no es valida")



