from flask import Blueprint, render_template, url_for, redirect, request
from model import Livro
from db import db

livros_bp = Blueprint("livros", __name__)

@livros_bp.route('/')
def home():
    try:
        livros = Livro.query.all()
        return render_template("index.html", livros=livros)
    except Exception as e:
            return f"Erro:{e}"
    
@livros_bp.route('/inserir', methods=["GET", "POST"])
def inserir():
    try:
        if request.method == "POST":
            titulo = request.form["titulo"]
            autor = request.form["autor"]
            ano = request.form["ano"]
            genero = request.form["genero"]
            livro = Livro(titulo=titulo, autor=autor, ano=ano, genero=genero)
            #livro = Livro(titulo=request.form["titulo"], autor=request.form["autor"], ano=request.form["ano"], genero=request.form["genero"])

            db.session.add(livro)
            db.session.commit()
            return redirect(url_for("livros.home"))
        return "Livros inseridos com sucesso"
    except Exception as e:
        return f"Erro:{e}"

@livros_bp.route('/deletar/<int:id>', methods=["GET", "POST"])
def deletar(id):
    try:
        if request.method == "POST":
            livro = db.session.get(Livro, id)
            db.session.delete(livro)
            db.session.commit()

            return redirect(url_for('livros.home'))
        return render_template("index.html")
    except Exception as e:
        return f"Erro:{e}"

@livros_bp.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id):
    try:
        livro = Livro.query.get(id)
        if request.method == "POST":
            livro.titulo = request.form["titulo"] # ou request.form.get('titulo')
            livro.autor = request.form["autor"] # ou request.form.get('autor')
            livro.ano = request.form["ano"] # ou request.form.get('ano')
            livro.genero = request.form["genero"] # ou request.form.get('genero')
            db.session.commit()
            return redirect(url_for('livros.home'))
        return render_template("editar.html", id_livro=id, livro=livro)
    except Exception as e:
            return f"Erro:{e}"