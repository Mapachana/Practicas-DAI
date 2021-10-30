#./app/app.py
from flask import Flask, render_template, request, redirect, session

import modelo 

app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

          
@app.route('/')
def hello_world():
    if 'username' in session:
        nombre = session['username']
    else:
        nombre = ''
    return render_template('index.html', username=nombre)

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
            return redirect('/login')
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

@app.route('/figuras')
def figuras():
    return render_template('figuras.html')




