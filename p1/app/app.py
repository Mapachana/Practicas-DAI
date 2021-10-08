#./app/app.py
from flask import Flask
import random

app = Flask(__name__)
          
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/jaja')
def prueba():
    return 'Esto es una prueba'

# Function to convert a list to string
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += str(ele)
        str1 += " "
    
    # return string  
    return str1 

# Asumo que ala lista se pasa como 1-2-3-5
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
