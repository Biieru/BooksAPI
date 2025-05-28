# BooksAPI

Uma API RESTful desenvolvida em Flask para gerenciamento de livros, com documentação Swagger integrada e testes automatizados.

## 🚀 Funcionalidades

- CRUD completo de livros
- Documentação automática com Swagger
- Testes automatizados com pytest
- Cobertura de testes monitorada
- Banco de dados SQLite com SQLAlchemy

## 📋 Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Biieru/BooksAPI.git
cd BooksAPI
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando o Projeto

1. Inicie o servidor:
```bash
python run.py
```

2. Acesse a documentação Swagger:
```
http://localhost:5000/apidocs
```

## 📚 Endpoints da API

### Livros

- `POST /books` - Adiciona um novo livro
- `GET /books` - Lista todos os livros
- `GET /books/<id>` - Obtém um livro específico
- `PUT /books/<id>` - Atualiza um livro
- `DELETE /books/<id>` - Remove um livro

## 🧪 Testes

Execute os testes com cobertura:
```bash
pytest --cov=app tests/
```

Cobertura atual:
- `app/__init__.py`: 100%
- `app/config.py`: 100%
- `app/controllers/book_controller.py`: 43%
- `app/models/book_model.py`: 90%
- `app/routes/book_routes.py`: 78%
- **Total**: 72%

## 🛠️ Tecnologias Utilizadas

- Flask
- SQLAlchemy
- Flasgger (Swagger)
- pytest
- pytest-flask
- pytest-cov

## 📝 Estrutura do Projeto

```
BooksAPI/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   └── book_controller.py
│   ├── models/
│   │   └── book_model.py
│   └── routes/
│       └── book_routes.py
├── tests/
│   └── test_books.py
├── requirements.txt
└── run.py
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
