from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', include('apps.aluno.urls')),
    path('matricula/', include('apps.matricula.urls')),
    path('professor/', include('apps.professor.urls')),
]
