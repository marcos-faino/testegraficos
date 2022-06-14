from django.urls import path
from . import views


urlpatterns = [
    path('', views.LivrosView.as_view(), name="livros")
]
