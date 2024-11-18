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
