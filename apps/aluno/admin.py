from django.contrib import admin
from .models import Aluno

# Registrando o Models no Admin do Django!
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    fields = ['nome', 'identidade', 'cpf', 'data_nascimento']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
