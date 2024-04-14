from django import forms
from .models import Agenda

class formularioAgenda(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('exame','medico','horario','consulData')