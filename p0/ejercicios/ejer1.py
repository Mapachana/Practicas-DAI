# Juego de adivinacion

import random

numero_magico = random.randint(1,100)
max_intentos = 10

print(numero_magico)

for i in range(0, max_intentos):
    numero = int(input("Intenta adivinar el numero  "))
    if numero == numero_magico:
        print("HAS ADIVINADO EL NUMERO!!")
        break