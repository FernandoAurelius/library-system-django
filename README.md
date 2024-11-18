# Sistema de Gerenciamento de Biblioteca Escolar

## Descrição

Este projeto é um sistema para organizar os livros da biblioteca da escola, desenvolvido em Python com Django. Ele permite o cadastro, consulta, atualização e remoção de livros. Além disso, registra as consultas realizadas pelos usuários. O sistema oferece uma interface intuitiva para facilitar a administração da biblioteca e a interação com os usuários.

---

## Funcionalidades

- **Cadastro de Livros**: Adicionar novos livros com detalhes como título, autor, ISBN, gênero, editora, data de publicação, resumo e disponibilidade.
- **Consulta de Livros**: Buscar livros usando filtros por título, autor, gênero, ou outros critérios.
- **Atualização de Livros**: Editar informações de livros, incluindo a alteração do status de disponibilidade.
- **Remoção de Livros**: Remover livros do sistema quando necessário.
- **Registro de Consultas**: Manter um histórico das interações entre usuários e livros.

---

## Diagrama de Classes UML

O diagrama de classes abaixo apresenta a modelagem do domínio do sistema:

```mermaid
classDiagram
    class Livro {
        +id: Integer
        +titulo: String
        +autor: String
        +isbn: String
        +genero: String
        +editora: String
        +disponibilidade: Boolean
        +data_publicacao: Date
        +resumo: Text
        +cadastrar(): void
        +consultar(): Livro
        +atualizar(): void
        +remover(): void
    }

    class Usuario {
        +id: Integer
        +nome: String
        +email: String
        +is_staff: Boolean
    }

    class Empréstimo {
        +id: Integer
        +usuario_id: Usuario
        +livro_id: Livro
        +data_consulta: DateTime
        +tipo_consulta: String
        +realizarConsulta(): void
    }

    Usuario "1" -- "0..*" Empréstimo : realiza
    Livro "1" -- "0..*" Empréstimo : é consultado em
```

## Tecnologias Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript (com Bootstrap para estilização)
- **Banco de Dados**: SQLite (padrão do Django, mas pode ser substituído por PostgreSQL ou MySQL)
- **Versionamento**: Git

---

## Requisitos

- Python 3.8 ou superior
- Django 4.0 ou superior
- Git

---

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/biblioteca-escolar.git
   cd biblioteca-escolar
   ```

2. ** Crie e ative um ambiente virtual
   ```bash
   python -m virtualenv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. ** Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. ** Configure o banco de dados:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. ** Inicie o servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```

6. ** Acesse o sistema: abra o navegador e vá para http://localhost:8000.

---

## Estrutura do Projeto
```plaintext
biblioteca-escolar/
├── biblioteca/               # Configurações principais do projeto Django
├── livros/                   # Aplicação Django responsável pela gestão de livros
│   ├── migrations/           # Arquivos de migração do banco de dados
│   ├── models.py             # Modelos das classes (Livro, Usuario, Consulta)
│   ├── views.py              # Lógica para atender às requisições
│   ├── urls.py               # Rotas da aplicação
│   └── templates/            # Arquivos HTML
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
├── manage.py                 # Script para gerenciar o projeto Django
└── requirements.txt          # Dependências do projeto
```
