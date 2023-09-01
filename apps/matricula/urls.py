from django.urls import path, include
from rest_framework import routers
from apps.matricula.api.viewsets import MatriculaViewSet

router = routers.DefaultRouter()
router.register('', MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('', include(router.urls)),
]
