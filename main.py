from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Base declarativa para os modelos
class Base(DeclarativeBase):
    pass

# Instanciando o SQLAlchemy com a base personalizada
db = SQLAlchemy(model_class=Base)

# Inicializando o Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# Modelo User
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

# Modelo Book
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]
    title: Mapped[str]

# Criando as tabelas do banco
with app.app_context():
    db.create_all()

# Rota simples
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Rota teste
@app.route("/teste")
def rota_teste():
    return "<p>Rota, teste!</p>"

# --------------------- ROTAS DO CRUD ------------------------

# Adicionar um livro (CREATE)
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Book(
        author=data["author"],
        genre=data["genre"],
        year=data["year"],
        title=data["title"]
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

# Listar todos os livros (READ - todos)
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [
        {
            "id": book.id,
            "author": book.author,
            "genre": book.genre,
            "year": book.year,
            "title": book.title
        } for book in books
    ]
    return jsonify(result)

# Buscar um livro por ID (READ - um)
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        "id": book.id,
        "author": book.author,
        "genre": book.genre,
        "year": book.year,
        "title": book.title
    })

# Atualizar um livro (UPDATE)
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.author = data.get("author", book.author)
    book.genre = data.get("genre", book.genre)
    book.year = data.get("year", book.year)
    book.title = data.get("title", book.title)

    db.session.commit()
    return jsonify({"message": "Livro atualizado com sucesso!"})

# Deletar um livro (DELETE)
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro removido com sucesso!"})