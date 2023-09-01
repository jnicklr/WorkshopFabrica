from django.db import models
from apps.professor.models import Professor

# Create your models here.

class Materia(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(verbose_name='Descrição')
    assunto = models.TextField()
    professor = models.ManyToManyField(Professor)

    def __str__(self):
        return f"{self.nome}, {self.professor.nome}"