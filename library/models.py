from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    isbn = models.CharField(max_length=17, null=False, blank=False, unique=True)
    genre = models.CharField(max_length=100, null=False, blank=False)
    publisher = models.CharField(max_length=100, null=False, blank=False)
    availability = models.BooleanField(null=False, blank=False, default=True)
    publication_date = models.DateField(null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    cover = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"Título do Livro: {self.title} | ID do Livro: {self.id}"

class Loan(models.Model):
    loan_date = models.DateField(null=False, blank=False)
    return_date = models.DateField(null=True, blank=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    returned = models.BooleanField(null=False, blank=False, default=False)