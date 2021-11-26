#./app/app.py
from flask import Flask, render_template, request, redirect, session, jsonify
from flask.wrappers import Request

import funciones

import modelo 
import modelo_pokemon


app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

   
@app.route('/')
def hello_world():
    argumentos = {}
    argumentos['error'] = ""
    db = modelo.Database()

    if 'username' in session:
        argumentos['username'] = session['username']

        datos_usuario = db.get_user(session['username'])
        argumentos['name'] = datos_usuario['name']

    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    return render_template('index.html', **argumentos)

'''
Practica 3
'''

@app.route('/mongo', methods=['GET', 'POST'])
def mongo():

    argumentos = {}
    argumentos['error'] = ""
    argumentos['lista_pokemon'] = []
    db = modelo.Database()

    if 'username' in session:
        argumentos['username'] = session['username']

        datos_usuario = db.get_user(session['username'])
        argumentos['name'] = datos_usuario['name']

    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    db = modelo_pokemon.DBPokemon()
	
    if request.method == 'POST':
        pokemons = db.buscar(request.form['texto']) # devuelve un cursor(*), no una lista ni un iterador
        for pokemon in pokemons:
            argumentos['lista_pokemon'].append(pokemon)

        return render_template('buscar.html', **argumentos)

    return render_template('buscar.html', **argumentos)

@app.route('/pokemon', methods=['POST'])
def add_pokemon():
    try:
        body = request.get_json(force=True)
        print(body)
    except:
        res = {'estado': "FAIL json invalido", 'codigo' : 400}
        return jsonify(res)

    if body is None:
        res ={'estado': "FAIL cuerpo vacio", 'codigo' : 400} 
    elif 'name' not in body or 'img' not in body or 'type' not in body or 'height' not in body or 'weight' not in body or 'candy' not in body or 'egg' not in body:
        res ={'estado': "FAIL Faltan datos. Se necesita nombre, img, tipo, altura, peso, chuche y huevo", 'codigo' : 400}
    else:
        db = modelo_pokemon.DBPokemon()
        id = db.add_pokemon(body['name'], body['img'], body['type'], body['height'], body['weight'], body['candy'], body['egg'])
        if id != None:
            res = {'estado' : "OK", 'codigo' : 200}
        else:
            res = {'estado' : "FAIL no se añade nada", 'codigo' : 400}
    return jsonify(res)

@app.route('/pokemon/<id>', methods=['PUT'])
def modify_pokemon(id):
    id = int(id)
    try:
        body = request.get_json(force=True)
        print(body)
    except:
        res = {'estado': "FAIL json invalido", 'codigo' : 400}
        return jsonify(res)

    if body is None:
        res ={'estado': "FAIL cuerpo vacio", 'codigo' : 400}
    elif 'name' not in body or 'img' not in body or 'type' not in body or 'height' not in body or 'weight' not in body or 'candy' not in body or 'egg' not in body:
        res ={'estado': "FAIL Faltan datos. Se necesita nombre, img, tipo, altura, peso, chuche y huevo", 'codigo' : 400}
    else:
        db = modelo_pokemon.DBPokemon()
        aux = db.modify_pokemon(id, body['name'], body['img'], body['type'], body['height'], body['weight'], body['candy'], body['egg'])
        if aux:
            res = {'estado' : "OK", 'codigo' : 200}
        else:
            res ={'estado': "FAIL no se actualiza nada", 'codigo' : 400}
    return jsonify(res)

@app.route('/pokemon/<id>', methods=['DELETE'])
def delete_pokemon(id):
    id = int(id)
    db = modelo_pokemon.DBPokemon()
    aux = db.delete_pokemon(id)
    if aux:
        res = {'estado' : "OK", 'codigo' : 200}
    else:
        res ={'estado': "FAIL no se borra nada", 'codigo' : 400}
    return jsonify(res)

@app.route('/pokemon/<id>', methods=['GET'])
def get_pokemon(id):
    id = int(id)
    db = modelo_pokemon.DBPokemon()
    poke = str(db.get_pokemon(id))
    if poke != "None":
        res = {'estado': "OK", 'codigo' : 200}
        res['pokemon'] = poke
        return jsonify(res)
    else:
        res = {'estado': "FAIL no se obtiene nada", 'codigo' : 400}
    return jsonify(res)


'''
Practica 2
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    argumentos = {}
    argumentos['error'] = ""
    db = modelo.Database()
    
    if request.method == 'POST':
        if request.form['username'] != "" and request.form['password'] and db.comprobar_login(request.form['username'], request.form['password']):
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    argumentos = {}
    argumentos['error'] = ""
    db = modelo.Database()
    
    if 'username' in session:
            return redirect("/")
    else:

        if request.method == 'POST':
            if request.form['username'] != '' and request.form['name'] != '' and request.form['password'] != '':
                if db.sign_up(request.form['username'], request.form['name'], request.form['password']):
                    session['username'] = request.form['username']
                    return redirect("/")
                else:
                    argumentos['error'] = "Todos los campos deben estar rellenos o el usuario ya existe"

        if 'username' in session:
            argumentos['username'] = session['username']
        else:
            argumentos['username'] = ''

        if 'ultimas_paginas' in session:
            argumentos['ultimaspaginas'] = session['ultimas_paginas']
        else:
            argumentos['ultimaspaginas'] = []


        return render_template('signup.html', **argumentos)


@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    argumentos = {}
    argumentos['error'] = ""
    db = modelo.Database()

    if 'username' in session:

        datos_usuario = db.get_user(session['username'])
        argumentos['name'] = datos_usuario['name']
        argumentos['password'] = datos_usuario['password']

        if request.method == 'POST':
            if request.form['name'] != '' and request.form['password'] != '':
                db.actualizar_user(session['username'], request.form['name'], request.form['password'])
                return redirect("/")
            else:
                argumentos['error'] = "Todos los campos deben estar rellenos"
    else:
        return redirect("/login")

    if 'username' in session:
        argumentos['username'] = session['username']
    else:
        argumentos['username'] = ''

    if 'ultimas_paginas' in session:
        argumentos['ultimaspaginas'] = session['ultimas_paginas']
    else:
        argumentos['ultimaspaginas'] = []

    return render_template('perfil.html', **argumentos)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "La has liado, esto es un 404, revisa la URL", 404

# Función para guardar cada peticion en la lista de ultimas paginas visitadas
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

'''
PRACTICA 1
'''


@app.route('/fibonacci/<fichero>')
def fibonacci_file(fichero):
    fichero_r = open(fichero, "r")
    n = int(fichero_r.read())
    fichero_r.close()

    salida = open("salida.txt", "w")
    salida.write(str(funciones.fibonacci(n)))
    salida.close()

    return "Se ha escrito el fichero"

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
    






