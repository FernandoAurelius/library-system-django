from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Obrigatório. Insira um endereço de e-mail válido.",
        widget=forms.EmailInput(attrs={"placeholder": "exemplo@email.com"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este endereço de e-mail já está em uso. Por favor, escolha outro.")
        return email

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # Inclui o campo email
        help_texts = {
            "username": "Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.",
        }
