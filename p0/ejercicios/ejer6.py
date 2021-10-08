# Expresiones regulares
import re
from typing import Pattern

p_nombre = "\w+\s[A-Z]"
p_email = "\w+@(hotmail|gmail|ugr|outlook)\.(com|es)"
p_tarjeta = "[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}"

def validar_nombre(texto):
    res = re.match(p_nombre, texto)
    if res:
        print("Texto es un nombre")
    else:
        print("Texto no es un nombre")

def validar_email(texto):
    res = re.match(p_email, texto)
    if res:
        print("Texto es un email")
    else:
        print("Texto no es un email")

def validar_tarjeta(texto):
    res = re.match(p_tarjeta, texto)
    if res:
        print("Texto es una tarjeta")
    else:
        print("Texto no es una tarjeta")


texto = input("Introduce el texto a validar: ")

validar_nombre(texto)
validar_email(texto)
validar_tarjeta(texto)
