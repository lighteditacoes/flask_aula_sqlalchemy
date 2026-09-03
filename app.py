from flask import Flask, render_template, redirect, url_for, request
from routes.livros import livros_bp
from flask_migrate import Migrate
from db import db
from model import Usuario, Livro


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estante.db'
db.init_app(app)

app.register_blueprint(livros_bp, url_prefix='/livros')

migrate=Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)