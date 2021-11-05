#./app/app.py
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request

import funciones
import random
import math

import modelo 


app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

          
@app.route('/')
def hello_world():
    argumentos = {}
    argumentos['error'] = ""

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    return render_template('index.html', **argumentos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    argumentos = {}
    argumentos['error'] = ""
    
    if request.method == 'POST':
        if modelo.comprobar_login(request.form['username'], request.form['password']):
            aux = request.form['username']
            session['username'] = aux
            print("entro aqui y vale")
            print(session['username'])
            return redirect('/')
        else:
            argumentos['error'] = "Los datos introducidos no son validos"

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []


    return render_template('login.html', **argumentos)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "La has liado, esto es un 404, revisa la URL", 404

@app.before_request
def guardar_paginas_visitadas():
    num_paginas = 3
    if 'ultimas_paginas' in session:
        pass
    else:
        session['ultimas_paginas'] = [''] * num_paginas 

    if request.path != "/favicon.ico" and request.method == "GET":
        aux = session['ultimas_paginas']

        for i in range(num_paginas-1, 0, -1):
            aux[i] = aux[i-1]

        aux[0] = request.url

        session['ultimas_paginas'] = aux


@app.route('/ordena', methods=['GET', 'POST'])
def burbuja():
    error = None
    argumentos = {}
    argumentos['error'] = ""
    argumentos['respuesta'] = ""
    
    if request.method == 'POST':
        if request.form['lista'] != '':
            lista = request.form['lista']
            argumentos['respuesta'] = funciones.burbuja(lista)

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []



    return render_template('ordena.html', **argumentos)


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
    res = funciones.listToString(vector_resultado)
    return res

@app.route('/fibonacci/<fichero>')
def fibonacci_file(fichero):
    fichero_r = open(fichero, "r")
    n = int(fichero_r.read())
    fichero_r.close()

    salida = open("salida.txt", "w")
    salida.write(str(funciones.fibonacci(n)))
    salida.close()

    return "Se ha escrito el fichero"

@app.route('/cadena/<n>')
def cadena(n):
    n = int(n)
    vec = [random.randint(0,2) for i in range(0,n)]
    res = ""

    for i in range(0,n):
        if vec[i] == 0:
            vec[i] = "["
        else:
            vec[i] = "]"

    res = res + "<p> La cadena generada es " + funciones.listToString(vec) + "</p>"

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
        res = res + "<p> Cadena válida </p>"
    else:
        res = res + "<p> Cadena NO válida </p>"

    return res


@app.route('/regex/<exp>')
def comprobar_regex(exp):
    res = ""
    if funciones.validar_nombre(exp):
        res = res + "<p>" + exp + " es un nombre"
    else:
        res = res + "<p>" + exp + " NO es un nombre"

    if funciones.validar_email(exp):
        res = res + "<p>" + exp + " es un email"
    else:
        res = res + "<p>" + exp + " NO es un email"

    if funciones.validar_tarjeta(exp):
        res = res + "<p>" + exp + " es una tarjeta"
    else:
        res = res + "<p>" + exp + " NO es una tarjeta"

    return res
    






