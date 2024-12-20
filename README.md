# 📚 Sistema de Gerenciamento de Biblioteca Escolar - BiblioTech

## ✨ Descrição
O **Sistema de Gerenciamento de Biblioteca Escolar (BiblioTech)** foi desenvolvido para modernizar e digitalizar o acervo da biblioteca do **Centro de Ensino Médio Integrado do Cruzeiro**.  
A plataforma oferece uma experiência digital amigável e eficiente para gerenciamento de livros, empréstimos e interação com os usuários, tornando a leitura mais acessível para estudantes e professores.  

🖥️ O projeto foi implementado com um backend robusto em **Python/Django**, banco de dados relacional gerenciado no **AWS RDS** (PostgreSQL), e deploy na nuvem utilizando **AWS EC2**, garantindo escalabilidade e confiabilidade como uma aplicação **Cloud-Native**.

---

## 📋 Funcionalidades

- 🔍 **Busca Avançada**: Pesquise por título, autor, gênero ou palavras-chave.
- 📖 **Gerenciamento de Livros**:  
  - Cadastro e atualização de informações.  
  - Status de disponibilidade (disponível ou emprestado).  
- ⏳ **Histórico de Empréstimos**: Controle de empréstimos e devoluções.  
- 🤖 **Recomendações Personalizadas**: Sugestões baseadas em históricos de consulta.  
- 📱 **Acesso Multidispositivo**: Interface responsiva para computadores, celulares e tablets.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.12+, Django 5.0+  
- **Frontend:** HTML5, CSS3, JavaScript (Bootstrap 5)  
- **Banco de Dados:** PostgreSQL (AWS RDS)  
- **Deploy:** AWS EC2 (backend) + AWS RDS  
- **Controle de Versão:** Git  

---

## 🧩 Diagrama de Classes UML

```mermaid
classDiagram
    direction TB
    class Book {
        +Integer id
        +String title
        +String author
        +String isbn
        +String genre
        +String publisher
        +Boolean availability
        +Date publication_date
        +String summary
        +String cover
        +__str__() String
    }
    class Loan {
        +Integer id
        +Date loan_date
        +Date return_date
        +Boolean returned
    }
    class User {
        <<DjangoModel>>
    }

    Book --> Loan : "1..* loans"
    User --> Loan : "1..* loans"
    Loan --> Book : "1 book"
    Loan --> User : "1 user"
```

## 📦 Estrutura do Projeto

```bash
$ tree

library-system-django/
├── setup/               # Configurações principais do projeto Django
├── library/                   # Aplicação principal (models, views, templates)
│   ├── migrations/           # Migrações do banco de dados
│   ├── admin.py              # Arquivo de definição da página de administração do projeto Django
│   ├── apps.py               # Definição do arquivo e dos módulos de configuração da app Django
│   ├── models.py             # Modelos de dados (Book, Loan)
│   ├── signals.py            # Gerencia ações automáticas em resposta a eventos específicos no sistema.         
│   ├── views.py              # Regras de negócio e lógicas de requisição
│   ├── utils.py              # Métodos úteis relacionados à app
│   ├── urls.py               # Rotas da aplicação
├── templates/                # Arquivos HTML
├── manage.py                 # Script de gerenciamento do Django
└── requirements.txt          # Dependências do projeto
```

---

## 📥 Instalação e Configuração

1. **Clone o repositório:**
    
    ```bash
    git clone https://github.com/FernandoAurelius/library-system-django.git
    cd library-system-django
    ```
    
2. **Crie e ative um ambiente virtual:**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
    
3. **Instale as dependências:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Configure o banco de dados (local ou remoto):**
    - Crie um banco PostgreSQL e adicione as variáveis de ambiente em um arquivo `.env`:
        
        ```env
        DATABASE_NAME=seu_banco
        DATABASE_USER=seu_usuario
        DATABASE_PASSWORD=sua_senha
        DATABASE_HOST=seu_host
        DATABASE_PORT=5432
        ```
        
5. **Aplique as migrações:**
    
    ```bash
    python manage.py migrate
    ```
    
6. **Crie um superusuário:**
    
    ```bash
    python manage.py createsuperuser
    ```
    
7. **Inicie o servidor de desenvolvimento:**
    
    ```bash
    python manage.py runserver
    ```
    
8. **Acesse a aplicação:** Abra o navegador e vá para `http://localhost:8000`.

---

## 🚀 Deploy

Este sistema foi implantado como uma aplicação **Cloud-Native** utilizando os serviços da **AWS**:

- 🖥️ **AWS EC2:** Backend hospedado.
- 🛢️ **AWS RDS (PostgreSQL):** Banco de dados escalável e gerenciado.
- 🔧 Configurações de produção:
    - Uso de `gunicorn` e `nginx` para servir o aplicativo.
    - Gerenciamento de variáveis de ambiente via `.env`.

---

## 🔮 Próximos Passos

- 📊 **Relatórios Avançados:** Geração de estatísticas de uso e popularidade dos livros.
- 📧 **Notificações por E-mail:** Lembretes automáticos para devoluções pendentes.
- 🌐 **Integração Social:** Login via redes sociais (Google, Facebook, etc.).

---

## 🤝 Contribuições

Contribuições são super bem-vindas! 💡

Se quiser colaborar:

1. Faça um *fork* do repositório.
2. Crie uma *branch* para sua funcionalidade.
3. Abra um *pull request* explicando suas alterações.

---

## ✨ Autores

- **FernandoAurelius** - Desenvolvedor
- **Centro de Ensino Médio Integrado do Cruzeiro** - Instituição parceira
