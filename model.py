from db import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable=True)
    idade = db.Column(db.Integer)
    email = db.Column(db.String(100))

class Livro(db.Model):
    id_livro = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable=True)
    autor = db.Column(db.String(50), nullable=True)
    ano = db.Column(db.String(4), nullable=True)
    genero = db.Column(db.String(50))