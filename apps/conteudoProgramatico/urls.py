from django.urls import path, include
from rest_framework import routers
from apps.conteudoProgramatico.api.viewsets import ConteudoProgramaticoViewSet

# Definindo a rota da API

router = routers.DefaultRouter()
router.register('', ConteudoProgramaticoViewSet, basename='conteudo')

urlpatterns = [
    path('', include(router.urls)),
]
