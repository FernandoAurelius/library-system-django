from django.db.models.signals import post_delete
from django.dispatch import receiver
from library.models import Loan

@receiver(post_delete, sender=Loan)
def set_book_availability(sender, instance, **kwargs):
    """
    Redefine a disponibilidade do livro associado quando um Loan é apagado.
    """
    book = instance.book
    book.availability = True
    book.save()
