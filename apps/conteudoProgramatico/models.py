from django.db import models
from apps.materia.models import Materia

# Create your models here.

class ConteudoProgramatico(models.Model):
    TURMA_CHOICES = (
        ('P1', 'Turma P1'),
        ('P2', 'Turma P2'),
        ('P3', 'Turma P3'),
        ('P4', 'Turma P4'),
        ('P5', 'Turma P5'),
        ('P6', 'Turma P6'),
        ('P7', 'Turma P7'),
        ('P8', 'Turma P8'),
    )
    area_do_conteudo = models.CharField(max_length=200) 
    periodo = models.CharField(max_length=2, choices=TURMA_CHOICES)
    materias = models.ManyToManyField(Materia)
    carga_horaria = property(lambda self: sum(materia.carga_horaria for materia in self.materias.all()))

    def __str__(self):
        return f"Conteúdo Programático {self.area_do_conteudo}, {self.periodo}"