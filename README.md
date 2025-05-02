# 📚 Projeto Flask com SQLAlchemy

Este é um projeto simples utilizando **Flask** e **SQLAlchemy** para gerenciar um banco de dados SQLite. O projeto define dois modelos básicos (`User` e `Book`) e expõe duas rotas de teste via HTTP.

## 🚀 Tecnologias Utilizadas

- **Flask** – Microframework web para Python.
- **SQLAlchemy** – ORM para comunicação com o banco de dados.

## 📁 Estrutura do Projeto
.
├── main.py
└── requirements.txt

### `main.py`

- Define a aplicação Flask.
- Configura o banco de dados SQLite (`project.db`).
- Cria dois modelos: `User` e `Book`.
- Cria as tabelas no banco de dados ao iniciar o app.
- Define duas rotas:
  - `/` retorna uma mensagem `"Hello, World!"`
  - `/teste` retorna uma mensagem `"Rota, teste!"`

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
