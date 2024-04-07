from django.urls import path,include
from . import views

urlpatterns = [
    path('consultas/', views.plataforma, name='consultas'),
    path('cadastro/', include('cadastroclient.urls'),name='cadastro')
]
