from django.db import models
from apps.conteudoProgramatico.models import ConteudoProgramatico

# Criação do Models!

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    mensalidade = models.IntegerField()
    tempo_conclusao = models.IntegerField()
    conteudo = models.ManyToManyField(ConteudoProgramatico)

    def __str__(self):
        return self.nome