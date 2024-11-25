from django.urls import path, include
from users.views import index, logout, SignUp, CustomLoginView, UserUpdateView


urlpatterns = [
    path("", index, name="index"),
    path("accounts/logout/", logout, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login", CustomLoginView.as_view(), name="login"),
    path("accounts/signup/", SignUp.as_view(), name="register"),
    path("accounts/profile/", UserUpdateView.as_view(), name="profile"),
]
