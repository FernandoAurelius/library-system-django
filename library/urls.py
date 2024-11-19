from django.urls import path
from library.views import LoanCreateView


urlpatterns = [
    path("create", LoanCreateView.as_view(), name="create")
]

