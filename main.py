from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #A classe BASE vai herdar tudo que esta implementado na DeclarativeBase
    pass

db = SQLAlchemy(model_class=Base) #Variavel que vai guardar o metodo SQLAlchemy usando como base a classe BASE

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db" # configurar o DB SQLite, relativo ao ao app

db.init_app(app) # Iniciando o app com a extensão

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model): # Model - O modelo da database, no caso, a formação das colunas dela
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]
    title: Mapped[str]

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def rota_teste():
    return "<p>Rota, teste!</p>"