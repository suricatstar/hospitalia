from django.shortcuts import redirect
from django.views.generic import ListView,CreateView
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agenda

# Create your views here.

class AgendaListView(LoginRequiredMixin,ListView):
    model = Agenda
    def get_queryset(self):
        # Filtra os agendamentos pelo usuário atualmente autenticado
        return Agenda.objects.filter(user=self.request.user)
    

class ConsultaCreateView(LoginRequiredMixin ,CreateView):
    model = Agenda
    fields= [
        "exame",
        "medico",
        "horario",
        "consulData",
    ]
    success_url = reverse_lazy('agenda')
    
    def form_valid(self, form):
        
        # Define o usuário atual como o usuário associado ao agendamento
        form.instance.user = self.request.user
        return super().form_valid(form)
    

def loginout(request):
    logout(request)
    return redirect(reverse('login_cliente'))