from django.db import models
from apps.conteudoProgramatico.models import ConteudoProgramatico

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    mensalidade = models.DecimalField(max_digits=5, decimal_places=2)
    tempo_conclusao = models.IntegerField()
    conteudo = models.ForeignKey(ConteudoProgramatico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome