from django.urls import path, include
from rest_framework import routers
from apps.aluno.api.viewsets import AlunoViewSet

router = routers.DefaultRouter()
router.register('', AlunoViewSet, basename='aluno')

urlpatterns = [
    path('', include(router.urls)),
]
