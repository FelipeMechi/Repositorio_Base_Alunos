# Exercicio 1.4: Rota com número (tipagem na rota)
# Crie uma rota /dobro/<int:numero> que recebe um número e retorna o dodro dele.

from flask import Flask, render_template
app = Flask(__name__) # representa o nome do  arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/') # @decorador de função
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Fábrica de Programadores'

@app.route('/zezinho') # para abrir a página precisamos adicionar o nome
def zezinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)