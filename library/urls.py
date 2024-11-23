from django.urls import path
from library.views import LoanCreateView, BookListView


urlpatterns = [
    path("emprestimos/criar", LoanCreateView.as_view(), name="loan_create"),
    path("livros", BookListView.as_view(), name="book_list"),
]

