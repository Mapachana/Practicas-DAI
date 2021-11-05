#./app/app.py
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request

import funciones

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

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    argumentos = {}
    argumentos['error'] = ""
    
    if request.method == 'POST':
        if 'username' in session:
            aux = session['username']
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


@app.route('/erastotenes', methods=['GET', 'POST'])
def erastotenes():
    argumentos = {}
    argumentos['error'] = ""
    argumentos['respuesta'] = ""
    
    if request.method == 'POST':
        if request.form['numero'] != '':
            lista = request.form['numero']
            argumentos['respuesta'] = funciones.erastotenes(lista)

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    return render_template('erastotenes.html', **argumentos)


@app.route('/fibonacci/<fichero>')
def fibonacci_file(fichero):
    fichero_r = open(fichero, "r")
    n = int(fichero_r.read())
    fichero_r.close()

    salida = open("salida.txt", "w")
    salida.write(str(funciones.fibonacci(n)))
    salida.close()

    return "Se ha escrito el fichero"


@app.route('/cadena', methods=['GET', 'POST'])
def cadena():
    argumentos = {}
    argumentos['error'] = ""
    argumentos['respuesta'] = ""
    
    if request.method == 'POST':
        if request.form['numero'] != '':
            lista = request.form['numero']
            argumentos['respuesta'] = funciones.cadena(lista)

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    return render_template('erastotenes.html', **argumentos)



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
    






