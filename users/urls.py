from django.urls import path, include
from users.views import index, logout, SignUp


urlpatterns = [
    path("", index, name="index"),
    path("accounts/logout/", logout, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name="register"),
]
