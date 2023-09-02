from django.db import models
from apps.conteudoProgramatico.models import ConteudoProgramatico

# Criação do Models!

class Curso(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    mensalidade = models.IntegerField(blank=False, null=False)
    tempo_conclusao = models.IntegerField(blank=False, null=False, verbose_name='Tempo de Conclusão')
    conteudo = models.ManyToManyField(ConteudoProgramatico)

    def __str__(self):
        return self.nome