from django.contrib import admin
from .models import Curso

# Registrando o Models no Admin do Django!
@admin.register(Curso)
class AlunoAdmin(admin.ModelAdmin):
    model = Curso
    fields = ['nome', 'mensalidade', 'tempo_conclusao', 'conteudo']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
