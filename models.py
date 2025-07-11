from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

class RegistroCorporal(db.Model):
    idRegistro = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    percentual_gordura = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)

class Refeicao(db.Model):
    idRefeicao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    horario = db.Column(db.DateTime, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    carboidratos = db.Column(db.Integer, nullable=False)
    proteinas = db.Column(db.Integer, nullable=False)
    gorduras = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)

class Treino(db.Model):
    idTreino = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)
