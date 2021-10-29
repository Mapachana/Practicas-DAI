#./app/app.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
          
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'prueba':
            error = 'Invalid credentials'
        else:
            return redirect('/')
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return "La has liado, esto es un 404, revisa la URL", 404

@app.route('/figuras')
def figuras():
    return render_template('figuras.html')




