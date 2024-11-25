from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm

from django.views.generic import CreateView

from django.contrib.auth.views import LoginView

from django.contrib import auth, messages

from django.http import HttpRequest

from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        messages.success(self.request, "Cadastro realizado com sucesso!")
        return super().form_valid(form)


class CustomLoginView(LoginView):
    success_url = reverse_lazy("book_list")
    template_name = "registration/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"Bem-vindo(a), seu login foi realizado com sucesso!")
        return super().form_valid(form)


def logout(request: HttpRequest):
    if request.method == "POST":
        auth.logout(request)
        return redirect("index")
    else:
        return render(request, "registration/logout.html")
    

def index(request: HttpRequest):
    return render(request, "index.html")
