from django.db import models

# Criação do Models!

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    area_atuacao = models.CharField(max_length=200, verbose_name='Area de Atuação', blank=False, null=False)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor da Hora', blank=False, null=False)

    def __str__(self):
        return self.nome