from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate
from db import db
from model import Usuario, Livro


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estante.db'
db.init_app(app)
migrate=Migrate(app, db)


@app.route('/')
def home():
    try:
        livros = Livro.query.all()
        return render_template("index.html", livros=livros)
    except Exception as e:
            return f"Erro:{e}"
    
@app.route('/inserir', methods=["GET", "POST"])
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
            return redirect(url_for("home"))
        return "Livros inseridos com sucesso"
    except Exception as e:
        return f"Erro:{e}"

@app.route('/deletar/<int:id>', methods=["GET", "POST"])
def deletar(id):
    try:
        if request.method == "POST":
            livro = db.session.get(Livro, id)
            db.session.delete(livro)
            db.session.commit()

            return redirect(url_for('home'))
        return render_template("index.html")
    except Exception as e:
        return f"Erro:{e}"

@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id):
    try:
        livro = Livro.query.get(id)
        if request.method == "POST":
            livro.titulo = request.form["titulo"] # ou request.form.get('titulo')
            livro.autor = request.form["autor"] # ou request.form.get('autor')
            livro.ano = request.form["ano"] # ou request.form.get('ano')
            livro.genero = request.form["genero"] # ou request.form.get('genero')
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("editar.html", id_livro=id, livro=livro)
    except Exception as e:
            return f"Erro:{e}"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)