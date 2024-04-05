from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_cliente/', views.cadastrarCliente,name='cadastrar_cliente'),
    path('login_cliente/', views.loginCliente, name='login_cliente')
]
