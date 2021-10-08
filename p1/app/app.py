#./app/app.py
from flask import Flask
import random
import math

app = Flask(__name__)
          
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/jaja')
def prueba():
    return 'Esto es una prueba'

# Function to convert a list to string
def listToString(s): 
    str1 = "" 
     
    for ele in s: 
        str1 += str(ele)
        str1 += " "
    
    return str1 

# Asumo que la lista se pasa como 1-2-3-5
@app.route('/ordena/<lista>')
def burbuja(lista):
    vector = lista.split('-')
    for i in range(len(vector)):
        vector[i] = int(vector[i])

    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i] < vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    res = listToString(vector)
    return res

@app.route('/erastotenes/<num>')
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

# FUncion de Fibonacci de un numero dado
def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci/<fichero>')
def fibonacci_file(fichero):
    fichero_r = open(fichero, "r")
    n = int(fichero_r.read())
    fichero_r.close()

    salida = open("salida.txt", "w")
    salida.write(str(fibonacci(n)))
    salida.close()

    return "Se ha escrito el fichero"

@app.route('/cadena')
def cadena():
    pass

@app.route('/regex/<exp>')
def comprobar_regex(exp):
    pass


