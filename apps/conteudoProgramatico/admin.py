from django.contrib import admin
from .models import ConteudoProgramatico

# Registrando o Models no Admin do Django!
@admin.register(ConteudoProgramatico)
class AlunoAdmin(admin.ModelAdmin):
    model = ConteudoProgramatico
    fields = ['area_do_conteudo', 'periodo', 'materias']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
