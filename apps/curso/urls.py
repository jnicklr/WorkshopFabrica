from django.urls import path, include
from rest_framework import routers
from apps.curso.api.viewsets import CursoViewSet

# Definindo a rota da API

router = routers.DefaultRouter()
router.register('', CursoViewSet, basename='curso')

urlpatterns = [
    path('', include(router.urls)),
]
