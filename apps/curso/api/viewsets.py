from rest_framework.viewsets import ModelViewSet
from .serializers import CursoSerializer
from apps.curso.models import Curso
from rest_framework.pagination import LimitOffsetPagination

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    pagination_class = LimitOffsetPagination