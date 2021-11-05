#./app/app.py
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request

import funciones

import modelo 


app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

          
@app.route('/')
def hello_world():
    if 'username' in session:
        nombre = session['username']
    else:
        nombre = ''

    if 'ultimas_paginas' in session:
        pags = session['ultimas_paginas']
    else:
        pags = ['prueba', 'prueba2', 'prueba3']
    return render_template('index.html', username=nombre, ultimaspaginas=pags)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    nombre = ""
    print("PRINT FUNCIONA")
    
    if request.method == 'POST':
        if modelo.comprobar_login(request.form['username'], request.form['password']):
            aux = request.form['username']
            session['username'] = aux
            print("entro aqui y vale")
            print(session['username'])
            return redirect('/')
        else:
            error = "Los datos introducidos no son validos"

    if 'username' in session:
        nombre = session['username']
        print(nombre)
    else:
        nombre = ''

    if 'ultimas_paginas' in session:
        pags = session['ultimas_paginas']
    else:
        pags = ['prueba', 'prueba2', 'prueba3']

    print(nombre)

    return render_template('login.html', username=nombre, ultimaspaginas=pags)

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
    nombre = ""
    res = ""
    
    if request.method == 'POST':
        if request.form['lista'] != '':
            lista = request.form['lista']
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

            res = funciones.listToString(vector)

    if 'username' in session:
        nombre = session['username']
    else:
        nombre = ''

    if 'ultimas_paginas' in session:
        pags = session['ultimas_paginas']
    else:
        pags = ['prueba', 'prueba2', 'prueba3']


    return render_template('ordena.html', username=nombre, ultimaspaginas=pags, respuesta=res)









