from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from library.models import Book, Loan
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import timedelta


# TODO: criar views da biblioteca
class OwnedMixin(LoginRequiredMixin):
  # def get_queryset(self, *args, **kwargs):
  #     return super().get_queryset(*args, **kwargs).filter(owner=self.request.user)

    def check_ownership(self, obj):
        if obj.owner != self.request.user:
            messages.error(
                self.request, "Você não tem permissão para modificar este empréstimo da biblioteca."
            )
            return False
        return True

    def set_owner(self, form):
        form.instance.owner = self.request.user
        return form


class LoanCreateView(OwnedMixin, CreateView):
    login_url = "accounts/login/"
    model = Loan
    fields = ["book", "return_date"]
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books_list"] = Book.objects.order_by("id").filter(availability=True)
        return context

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields["book"].queryset = Book.objects.order_by("id").filter(availability=True)
        form.fields["book"].label = "Livros disponíveis para empréstimo"
        form.fields["return_date"].label = "Data de devolução"
        form.fields["return_date"].help_text = "Insira a data no formato: dd/mm/aaaa"
        return form

    def form_valid(self, form):
        form = self.set_owner(form)
        return_date = form.cleaned_data.get("return_date")
        month_ahead = (timezone.now() + timedelta(days=30)).date()
        today = timezone.now().date()
        if return_date > month_ahead or return_date <= today:
            today = timezone.now().date()
            today = today.strftime("%d/%m/%Y")
            month_ahead = month_ahead.strftime("%d/%m/%Y")
            form.add_error(
                "return_date",
                f"O prazo de entrega do livro precisa ser entre a data de hoje ({today}) e o próximo mês ({month_ahead}).",
            )
            return self.form_invalid(form)
        form.instance.loan_date = timezone.now()
        form.instance.user = self.request.user
        book = form.instance.book
        if book.availability == False:
            form.add_error(
                "book",
                "O livro está indisponível para empréstimo. Por favor, escolha outro título."
            )
            return self.form_invalid(form)
        book.availability = False
        book.save()
        return super().form_valid(form)


class BookListView(OwnedMixin, ListView):
    login_url = "accounts/login"
    model = Book
    # fields = ["title", "author", "genre", "summary", "availability"]
