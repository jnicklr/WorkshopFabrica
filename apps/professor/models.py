from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    area_atuacao = models.CharField(max_length=200, verbose_name='Area de Atuação')
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome