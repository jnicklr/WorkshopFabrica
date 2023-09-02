from django.urls import path, include
from rest_framework import routers
from apps.professor.api.viewsets import ProfessorViewSet

# Definindo a rota da API

router = routers.DefaultRouter()
router.register('', ProfessorViewSet, basename='professor')

urlpatterns = [
    path('', include(router.urls)),
]
