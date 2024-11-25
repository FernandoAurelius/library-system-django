from django.urls import path
from library.views import LoanCreateView, LoanUpdateView, BookListView


urlpatterns = [
    path("emprestimos/criar", LoanCreateView.as_view(), name="loan_create"),
    path("emprestimos/atualizar/<int:pk>", LoanUpdateView.as_view(), name="loan_update"),
    path("livros", BookListView.as_view(), name="book_list"),
]
