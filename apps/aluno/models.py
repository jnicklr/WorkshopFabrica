from django.db import models
from django.core.exceptions import ValidationError

# Criação do Models!

# Função simples para validar se o CPF escrito é númerico e atinge a quantidade de caracteres correta!
def validar_cpf(value):
    if len(value) != 14 or not value.replace(".", "").replace("-", "").isdigit():
        raise ValidationError('O CPF deve estar no formato "xxx.xxx.xxx-xxx".')

class Aluno(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    identidade = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, help_text='O formato deve ser: xxx.xxx.xxx-xxx', validators=[validar_cpf], verbose_name='CPF')
    data_nascimento = models.DateField(blank=False, null=False, verbose_name='Data de Nascimento')

    def __str__(self):
        return self.nome