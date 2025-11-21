from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou um aluno do projeto Fábrica de Programadores'

@app.route('/lista') 
def lista():
    alunos = ['Abed','Raphael','Helena','Renan','Felipe','Enzo','Guilherme','Jorge','Igor','Emanuel','Caio']
    return render_template('ex_3-2.html', lista=alunos)

if __name__ == '__main__':
    app.run(debug=True)