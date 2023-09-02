from django.contrib import admin
from .models import Materia

# Registrando o Models no Admin do Django!
@admin.register(Materia)
class AlunoAdmin(admin.ModelAdmin):
    model = Materia
    fields = ['nome', 'descricao', 'assunto', 'professor', 'carga_horaria']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
