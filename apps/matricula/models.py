from django.db import models
from apps.aluno.models import Aluno

# Create your models here.

class Matricula(models.Model):
    TURMA_CHOICES = (
        ('a', 'Turma A'),
        ('b', 'Turma B'),
        ('c', 'Turma C'),
        ('d', 'Turma D'),
    )
    data_matricula = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    turma = models.CharField(max_length=1, choices=TURMA_CHOICES)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aluno.nome}, {self.data_matricula}"