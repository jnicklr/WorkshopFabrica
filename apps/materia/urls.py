from django.urls import path, include
from rest_framework import routers
from apps.materia.api.viewsets import MateriaViewSet

router = routers.DefaultRouter()
router.register('', MateriaViewSet, basename='materia')

urlpatterns = [
    path('', include(router.urls)),
]
