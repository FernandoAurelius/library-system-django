from library.models import Loan

def delete_loans():
    loans = Loan.objects.all()
    for loan in loans:
        loan.delete()

def db_seed():
    from library.models import Book
    from datetime import date


    Book.objects.all().delete()


    books = [
        
        {
            "title": "A Sociedade do Anel",
            "author": "J.R.R. Tolkien",
            "isbn": "9780007525546",
            "genre": "Fantasia",
            "publisher": "HarperCollins",
            "availability": True,
            "publication_date": date(1954, 7, 29),
            "summary": "O primeiro volume da épica trilogia 'O Senhor dos Anéis'.",
            "cover": "https://m.media-amazon.com/images/I/81hCVEC0ExL._AC_UF1000,1000_QL80_.jpg"  
        },
        {
            "title": "As Duas Torres",
            "author": "J.R.R. Tolkien",
            "isbn": "9780007525553",
            "genre": "Fantasia",
            "publisher": "HarperCollins",
            "availability": True,
            "publication_date": date(1954, 11, 11),
            "summary": "O segundo volume da épica trilogia 'O Senhor dos Anéis'.",
            "cover": "https://m.media-amazon.com/images/I/81lQ5N0QwJL._AC_UF1000,1000_QL80_.jpg"  
        },
        {
            "title": "O Retorno do Rei",
            "author": "J.R.R. Tolkien",
            "isbn": "9780007525560",
            "genre": "Fantasia",
            "publisher": "HarperCollins",
            "availability": True,
            "publication_date": date(1955, 10, 20),
            "summary": "O terceiro volume da épica trilogia 'O Senhor dos Anéis'.",
            "cover": "https://m.media-amazon.com/images/I/71+4uDgt8JL._AC_UF1000,1000_QL80_.jpg"  
        },

        
        {
            "title": "O Silmarillion",
            "author": "J.R.R. Tolkien",
            "isbn": "9780261102736",
            "genre": "Fantasia",
            "publisher": "George Allen & Unwin",
            "availability": True,
            "publication_date": date(1977, 9, 15),
            "summary": "A história dos Dias Antigos, antes de 'O Senhor dos Anéis'.",
            "cover": "https://harpercollins.com.br/cdn/shop/products/9786560050013.jpg?v=1704096160"  
        },
        {
            "title": "Beren e Lúthien",
            "author": "J.R.R. Tolkien",
            "isbn": "9781328791825",
            "genre": "Fantasia",
            "publisher": "HarperCollins",
            "availability": True,
            "publication_date": date(2017, 6, 1),
            "summary": "A história épica de Beren e Lúthien.",
            "cover": "https://dcdn.mitiendanube.com/stores/004/783/147/products/3-e9888ea5245a5306c417261497545571-1024-1024.png"  
        },
        {
            "title": "A Queda de Gondolin",
            "author": "J.R.R. Tolkien",
            "isbn": "9780008302757",
            "genre": "Fantasia",
            "publisher": "HarperCollins",
            "availability": True,
            "publication_date": date(2018, 8, 30),
            "summary": "A destruição de uma cidade élfica durante a Primeira Era.",
            "cover": "https://harpercollins.com.br/cdn/shop/products/9788595084148_1469cfff-4e53-4e09-93fc-c0596a83a77e.jpg?v=1686059634"  
        },

        
        {
            "title": "Duna",
            "author": "Frank Herbert",
            "isbn": "9780441013593",
            "genre": "Ficção Científica",
            "publisher": "Ace",
            "availability": True,
            "publication_date": date(1965, 8, 1),
            "summary": "Um épico de ficção científica em um deserto planetário.",
            "cover": "https://m.media-amazon.com/images/I/81SPvywH9sL._AC_UF1000,1000_QL80_.jpg"  
        },
        {
            "title": "Messias de Duna",
            "author": "Frank Herbert",
            "isbn": "9780441172696",
            "genre": "Ficção Científica",
            "publisher": "Ace",
            "availability": True,
            "publication_date": date(1969, 7, 1),
            "summary": "O segundo livro da saga Duna.",
            "cover": "https://m.media-amazon.com/images/I/91SSz053P0L._AC_UF1000,1000_QL80_.jpg"  
        },

        
        {
            "title": "Fundação",
            "author": "Isaac Asimov",
            "isbn": "9780553293357",
            "genre": "Ficção Científica",
            "publisher": "Spectra",
            "availability": True,
            "publication_date": date(1951, 6, 1),
            "summary": "A primeira obra da série 'Fundação', de Isaac Asimov.",
            "cover": "https://editoraaleph.com.br/cdn/shop/files/capas_site_700x1000_Fundacao.png?v=1714169773&width=700"  
        },
        {
            "title": "Fundação e Império",
            "author": "Isaac Asimov",
            "isbn": "9780553293371",
            "genre": "Ficção Científica",
            "publisher": "Spectra",
            "availability": True,
            "publication_date": date(1952, 6, 1),
            "summary": "O segundo livro da série 'Fundação'.",
            "cover": "https://editoraaleph.com.br/cdn/shop/products/unnamed_1fa8fd8f-57fc-4f55-80e6-8e81fc19d9a0.jpg?v=1687527340&width=667"  
        },

        
        {
            "title": "Crime e Castigo",
            "author": "Fiódor Dostoiévski",
            "isbn": "9780140449136",
            "genre": "Romance",
            "publisher": "Penguin Classics",
            "availability": True,
            "publication_date": date(1866, 1, 1),
            "summary": "Um clássico sobre moralidade e crime.",
            "cover": "https://m.media-amazon.com/images/I/81+dpv22LGL._AC_UF1000,1000_QL80_.jpg"  
        },
        {
            "title": "Os Irmãos Karamazov",
            "author": "Fiódor Dostoiévski",
            "isbn": "9780140449242",
            "genre": "Romance",
            "publisher": "Penguin Classics",
            "availability": True,
            "publication_date": date(1880, 1, 1),
            "summary": "A história dos irmãos Karamazov.",
            "cover": "https://m.media-amazon.com/images/I/81s51UO4t6L._AC_UF1000,1000_QL80_.jpg"  
        },

        
        {
            "title": "Meditações",
            "author": "Marco Aurélio",
            "isbn": "9780812968255",
            "genre": "Filosofia",
            "publisher": "Modern Library",
            "availability": True,
            "publication_date": date(180, 1, 1),
            "summary": "Reflexões estoicas do imperador romano Marco Aurélio.",
            "cover": "https://m.media-amazon.com/images/I/612B0id4gNL._AC_UF1000,1000_QL80_.jpg"  
        },

        
        {
            "title": "Assim Falou Zaratustra",
            "author": "Friedrich Nietzsche",
            "isbn": "9780140441185",
            "genre": "Filosofia",
            "publisher": "Penguin Classics",
            "availability": True,
            "publication_date": date(1883, 1, 1),
            "summary": "Uma obra filosófica sobre o conceito do super-homem.",
            "cover": "https://m.media-amazon.com/images/I/81BSagUOucL._UF894,1000_QL80_.jpg"  
        },
            {
            "title": "A Guerra dos Tronos",
            "author": "George R.R. Martin",
            "isbn": "9780553103540",
            "genre": "Fantasia",
            "publisher": "Bantam Books",
            "availability": True,
            "publication_date": date(1996, 8, 6),
            "summary": "O primeiro livro da série 'As Crônicas de Gelo e Fogo', apresentando Westeros e sua política intrigante.",
            "cover": "https://m.media-amazon.com/images/I/91+1SUO3vUL.jpg"
        },
        {
            "title": "A Fúria dos Reis",
            "author": "George R.R. Martin",
            "isbn": "9780553108033",
            "genre": "Fantasia",
            "publisher": "Bantam Books",
            "availability": True,
            "publication_date": date(1998, 11, 16),
            "summary": "O segundo livro da série, explorando os conflitos que surgem após a morte do rei Robert Baratheon.",
            "cover": "https://m.media-amazon.com/images/I/91PglZzF9kL.jpg"
        },
        {
            "title": "A Tormenta de Espadas",
            "author": "George R.R. Martin",
            "isbn": "9780553106633",
            "genre": "Fantasia",
            "publisher": "Bantam Books",
            "availability": True,
            "publication_date": date(2000, 8, 8),
            "summary": "O terceiro livro da série, com eventos dramáticos como o Casamento Vermelho.",
            "cover": "https://m.media-amazon.com/images/I/912SYaebhuL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "title": "O Festim dos Corvos",
            "author": "George R.R. Martin",
            "isbn": "9780553801507",
            "genre": "Fantasia",
            "publisher": "Bantam Books",
            "availability": True,
            "publication_date": date(2005, 10, 17),
            "summary": "O quarto livro da série, focando na reconstrução de Westeros após a Guerra dos Cinco Reis.",
            "cover": "https://m.media-amazon.com/images/I/915n69YKrCL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "title": "A Dança dos Dragões",
            "author": "George R.R. Martin",
            "isbn": "9780553801477",
            "genre": "Fantasia",
            "publisher": "Bantam Books",
            "availability": True,
            "publication_date": date(2011, 7, 12),
            "summary": "O quinto livro da série, trazendo de volta Daenerys Targaryen e sua jornada.",
            "cover": "https://m.media-amazon.com/images/I/91gIftSmvhL._AC_UF1000,1000_QL80_.jpg"
        }
    ]


    for book in books:
        Book.objects.create(**book)

    print(f"{len(books)} livros adicionados com sucesso!")

