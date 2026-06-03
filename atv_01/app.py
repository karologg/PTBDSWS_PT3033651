
from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>' .format(user_agent)

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return '<p>Bad request</p>', 400

@app.route('/objetoresposta')
def objeto_resposta():
    return '<h1>This document carries a cookie!</h1>'

@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://youtu.be/T1ql5mqnCp0?si=VpjKcsp0tCm_dinq')

@app.route('/abortar')
def get_user(id):
    abort(404)
