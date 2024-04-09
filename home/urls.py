from django.urls import path,include
from . import views
from .views import AgendaListView,ConsultaCreateView

urlpatterns = [
    path('logout/',views.loginout, name='loginout'),
    path('consultas/', ConsultaCreateView.as_view(), name='consultas'),
    path('agenda/', AgendaListView.as_view(), name='agenda'),
    path('cadastro/', include('cadastroclient.urls'),name='cadastros')
]
