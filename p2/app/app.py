#./app/app.py
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request

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
        pags = []
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
    print(nombre)

    return render_template('login.html', username=nombre)

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
        session['ultimas_paginas'] = []

    print(len(session['ultimas_paginas']))

    '''if len(session['ultimas_paginas']) < num_paginas:
        aux = session['ultimas_paginas']
        aux.append(Request.url)
        session['ultimas_paginas'] = aux
    else:
        for i in range(1,num_paginas):
            session['ultimas_paginas'][i] = session['ultimas_paginas'][i-1]
        session['ultimas_paginas'][0] = request.url

    print(session['ultimas_paginas']'''











