from django.db import models
from apps.professor.models import Professor

# Criação do Models!

class Materia(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descrição', blank=False, null=False)
    assunto = models.TextField(blank=False, null=False)
    professor = models.ManyToManyField(Professor)
    carga_horaria = models.IntegerField(verbose_name='Carga Horária', blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"