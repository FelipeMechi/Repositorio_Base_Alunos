
from flask import Flask, render_template
app = Flask(__name__) # representa o nome do  arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/') # @decorador de função
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou um aluno do projeto Fábrica de Programadores'

@app.route('/saudacao/<nome>') # para abrir a página precisamos adicionar o nome
def saudacao(nome):
    return f'Olá {nome}! Seja bem-vindo(a)?'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    dobro = numero*2
    return f'O dobro de {numero} é {dobro}'

if __name__ == '__main__':
    app.run(debug=True)