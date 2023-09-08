from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
