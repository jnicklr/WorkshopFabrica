from django.db import models
from apps.aluno.models import Aluno
from apps.curso.models import Curso

# Criação do Models!

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
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    # A classe property serve para declarar uma determinada variável como uma
    # propriedade normal, ou seja, é possível desenvolver um método personalizado
    # que se comporta como um campo do modelo
    
    # O método a seguir calcula o valor total do curso que o usuário vai investir
    # Exemplo: um curso de ciência da computação dura 4 anos e tem mensalidade 300
    # a função vai calcular o custo baseado nesses valores, mensalidade (300) * total de meses (4 * 12)
    @property
    def custo(self):
        return self.curso.mensalidade * (self.curso.tempo_conclusao * 12)

    def __str__(self):
        return f"{self.aluno.nome}, {self.data_matricula}"