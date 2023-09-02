from django.db import models
from apps.professor.models import Professor

# Criação do Models!

class Materia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(verbose_name='Descrição')
    assunto = models.TextField()
    professor = models.ManyToManyField(Professor)
    carga_horaria = models.IntegerField(verbose_name='Carga Horária')

    def __str__(self):
        return f"{self.nome}"