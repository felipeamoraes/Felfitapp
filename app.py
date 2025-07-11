from flask import Flask, request, render_template, redirect, url_for
from models import db, User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SECRET_KEY'] = 'segredo'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/cadastrar', methods=[ 'POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    peso = request.form['peso']
    altura = request.form['altura']
    idade = request.form['idade']
    novo = User(nome=nome, email=email, peso=peso, altura=altura, idade=idade)

    user = User(nome=nome, email=email, peso=peso, altura=altura, idade=idade)
    db.session.add(novo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    arquivo = request.files['foto']
    nomearquivo = file.filename
    caminho = os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename)
   # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)