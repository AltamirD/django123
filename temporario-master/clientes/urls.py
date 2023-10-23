from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('sair/', views.deslogar, name="deslogar")
]