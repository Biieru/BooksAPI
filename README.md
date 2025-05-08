# 📚 Projeto Flask com SQLAlchemy

Este é um projeto simples utilizando **Flask** e **SQLAlchemy** para gerenciar um banco de dados SQLite. O projeto define dois modelos básicos (`User` e `Book`) e expõe uma API REST para manipulação de livros.

## 🚀 Tecnologias Utilizadas

- **Flask** – Microframework web para Python.
- **SQLAlchemy** – ORM para comunicação com o banco de dados.
- **SQLite** – Banco de dados leve, utilizado localmente.

## 📁 Estrutura do Projeto
├── main.py

└── requirements.txt

└── project.db (Gerado automaticamente ao rodar o app)


### `main.py`

- Define a aplicação Flask.
- Configura o banco de dados SQLite (`project.db`).
- Cria dois modelos: `User` e `Book`.
- Cria as tabelas no banco de dados ao iniciar o app.
- Define rotas HTTP, incluindo uma API REST completa para o modelo `Book`.

---

## 🧩 Modelos

### `User`

| Campo    | Tipo     | Restrições   |
|----------|----------|--------------|
| id       | Integer  | Primary Key  |
| username | String   | Único        |
| email    | String   | -            |

### `Book`

| Campo  | Tipo    | Restrições  |
|--------|---------|-------------|
| id     | Integer | Primary Key |
| author | String  | -           |
| genre  | String  | -           |
| year   | Integer | -           |
| title  | String  | -           |

---

## 🔗 Rotas Disponíveis

### 📌 Rotas de Teste

| Método | Rota     | Descrição                |
|--------|----------|--------------------------|
| GET    | `/`      | Retorna `Hello, World!`  |
| GET    | `/teste` | Retorna `Rota, teste!`   |

---

### 📚 API REST para `Book`

| Método | Rota             | Descrição                       |
|--------|------------------|----------------------------------|
| POST   | `/books`         | Adiciona um novo livro           |
| GET    | `/books`         | Retorna todos os livros          |
| GET    | `/books/<id>`    | Retorna um livro específico      |
| PUT    | `/books/<id>`    | Atualiza um livro existente      |
| DELETE | `/
