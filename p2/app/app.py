#./app/app.py
from flask import Flask, render_template


app = Flask(__name__)
          
@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.errorhandler(404)
def page_not_found(e):
    return "La has liado, esto es un 404, revisa la URL", 404

@app.route('/figuras')
def figuras():
    return render_template('figuras.html')




