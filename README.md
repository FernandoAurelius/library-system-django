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
        +id: AutoField
        +titulo: CharField
        +autor: CharField
        +isbn: CharField
        +genero: CharField
        +editora: CharField
        +disponibilidade: BooleanField
        +data_publicacao: DateField
        +resumo: TextField
    }

    class Usuario {
        +id: AutoField
        +nome: CharField
        +email: EmailField
        +is_staff: BooleanField
    }

    class Emprestimo {
        +id: AutoField
        +usuario: ForeignKey(Usuario)
        +livro: ForeignKey(Livro)
        +data_emprestimo: DateTimeField
        +data_devolucao: DateTimeField
        +realizar_emprestimo(): None
        +registrar_devolucao(): None
    }

    Usuario "1" -- "0..*" Emprestimo : realiza
    Livro "1" -- "0..*" Emprestimo : é emprestado em
```

## Tecnologias Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML e CSS (com Bootstrap para estilização)
- **Banco de Dados**: PostgreSQL
- **Versionamento**: Git
- **Deploy**: AWS Lightsail, AWS RDS

---

## Requisitos

- Python 3.8 ou superior
- Django 4.0 ou superior
- SQLite ou PostgreSQL com pgAdmin ou PSQL
- Git

---

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/FernandoAurelius/library-system-django.git
   cd library-system-django
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
library-system-django/
├── setup/               # Configurações principais do projeto Django
├── library/                   # Aplicação Django responsável pela gestão de livros
│   ├── migrations/           # Arquivos de migração do banco de dados
│   ├── models.py             # Modelos das classes (Livro, Usuario, Empréstimo)
│   ├── views.py              # Lógica para atender às requisições
│   ├── urls.py               # Rotas da aplicação
│   └── templates/            # Arquivos HTML
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
├── manage.py                 # Script para gerenciar o projeto Django
└── requirements.txt          # Dependências do projeto
```
