from django.contrib import admin
from .models import Professor

# Registrando o Models no Admin do Django!
@admin.register(Professor)
class AlunoAdmin(admin.ModelAdmin):
    model = Professor
    fields = ['nome', 'area_atuacao', 'valor_hora']

# Outro método para registrar o model no Admin:
# admin.site.register(Aluno)
