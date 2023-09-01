from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    identidade = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome