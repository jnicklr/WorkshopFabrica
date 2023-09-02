from django.contrib import admin
from django.urls import path, include

# Rotas para a utilização das APIs:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', include('apps.aluno.urls')),
    path('matricula/', include('apps.matricula.urls')),
    path('professor/', include('apps.professor.urls')),
    path('materia/', include('apps.materia.urls')),
    path('conteudo/', include('apps.conteudoProgramatico.urls')),
    path('curso/', include('apps.curso.urls')),
]
