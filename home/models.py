from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agenda(models.Model):
    exame = models.CharField(max_length=60,null=False)
    medico = models.CharField(max_length=60,null=False)
    horario = models.CharField(max_length=60,null=False)
    marcaData = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    consulData = models.DateField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.exame