import re
from typing import Pattern
import math
import random

# Function to convert a list to string
def listToString(s): 
    str1 = "" 
     
    for ele in s: 
        str1 += str(ele)
        str1 += " "
    
    return str1 

# FUncion de Fibonacci de un numero dado
def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Expresiones regulares para comprobar
p_nombre = "\w+\s[A-Z]"
p_email = "\w+@(hotmail|gmail|ugr|outlook)\.(com|es)"
p_tarjeta = "[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}"

# Función para comprobar si una cadena es un nombre
def validar_nombre(texto):
    res = re.match(p_nombre, texto)
    return res

# Función para comprobar si una cadena es un email
def validar_email(texto):
    res = re.match(p_email, texto)
    return res

# Función para comprobar si una cadena es una tarjeta
def validar_tarjeta(texto):
    res = re.match(p_tarjeta, texto)
    return res

# Funcion para ordenar un string dado como numeros separados por guiones tal que 4-2-3
def burbuja(lista):
    vector = lista.split('-')
    for i in range(len(vector)):
        if vector[i] != '':
            vector[i] = int(vector[i])
        else:
            vector[i] = 0

    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i] < vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    res = listToString(vector)
    return res

# Funcion para hacer la funcion de erastotenes
def erastotenes(num):
    num = int(num)
    long = int(math.sqrt(num))+1

    vec = [False for i in range(0, num)]
    vector_resultado = []

    for i in range(2, long):
        for j in range(i, int(num/i)+1):
            if (i*j) < num:
                vec[i*j] = True

    for i in range(2, num):
        if not vec[i]:
            vector_resultado.append(i)
    res = listToString(vector_resultado)
    return res

# Funcion para hacer la funcion de validar cadenas
def cadena(n):
    n = int(n)
    vec = [random.randint(0,2) for i in range(0,n)]
    res = ""

    for i in range(0,n):
        if vec[i] == 0:
            vec[i] = "["
        else:
            vec[i] = "]"

    res = res + "La cadena generada es " + listToString(vec)

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
        res = res + "Cadena válida"
    else:
        res = res + "Cadena NO válida"

    return res