from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm

from library.models import Loan

from django.views.generic import CreateView, UpdateView

from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("book_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        del context["form"].fields["password"]
        del context["form"].fields["last_login"]
        del context["form"].fields["first_name"]
        del context["form"].fields["last_name"]
        del context["form"].fields["is_staff"]
        del context["form"].fields["is_active"]
        del context["form"].fields["date_joined"]
        del context["form"].fields["is_superuser"]
        del context["form"].fields["groups"]
        del context["form"].fields["user_permissions"]

        user_loans = Loan.objects.filter(user = self.request.user)
        context["user_loans"] = user_loans

        return context

    def get_object(self):
        return self.request.user


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
