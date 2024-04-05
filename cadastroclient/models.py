from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome= models.CharField(max_length=60, null=False)
    cpf= models.IntegerField(null=False)
    idade= models.IntegerField(null=False)
    email= models.CharField(max_length=30,null=True)
    numero= models.IntegerField(null=True)
    
    def __str__(self):
        return self.nome