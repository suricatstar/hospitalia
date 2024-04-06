from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrarCliente,name='cadastrar_cliente'),
    path('login/', views.loginCliente, name='login_cliente')
]
