from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome= models.CharField(max_length=60, null=False)
    cpf= models.IntegerField()
    idade= models.IntegerField(null=True,blank=True)
    numero= models.IntegerField(null=True,blank=True)
    email= models.CharField(max_length=30,null=False)
    senha= models.CharField(max_length=20,null=False)
    
    
    def __str__(self):
        return self.nome