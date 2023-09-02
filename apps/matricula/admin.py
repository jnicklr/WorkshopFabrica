from django.contrib import admin
from .models import Matricula

# Registrando o Models no Admin do Django!
@admin.register(Matricula)
class AlunoAdmin(admin.ModelAdmin):
    model = Matricula
    fields = ['id', 'data_matricula', 'valor', 'turma', 'aluno', 'curso']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
