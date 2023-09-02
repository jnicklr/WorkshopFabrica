from django.db import models
from apps.materia.models import Materia

# Criação do Models!

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
        ('P9', 'Turma P9'),
        ('P10', 'Turma P10'),
    )
    area_do_conteudo = models.CharField(max_length=200) 
    periodo = models.CharField(max_length=3, choices=TURMA_CHOICES)
    materias = models.ManyToManyField(Materia)

    # A classe property serve para declarar uma determinada variável como uma
    # propriedade normal, ou seja, é possível desenvolver um método personalizado
    # que se comporta como um campo do modelo

    # O método a seguir faz a soma de todas as cargas horárias das matérias
    # que estão presentes na classe Materia que foi selecionada, e armazena o valor
    # no atributo carga horária da classe ConteudoProgramatico
    carga_horaria = property(lambda self: sum(materia.carga_horaria for materia in self.materias.all()))

    def __str__(self):
        return f"Conteúdo Programático {self.area_do_conteudo}, {self.periodo}, {self.carga_horaria}"