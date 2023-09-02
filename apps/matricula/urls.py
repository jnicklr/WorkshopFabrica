from django.urls import path, include
from rest_framework import routers
from apps.matricula.api.viewsets import MatriculaViewSet

# Definindo a rota da API

router = routers.DefaultRouter()
router.register('', MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('', include(router.urls)),
]
