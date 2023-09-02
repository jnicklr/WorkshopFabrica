from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CursoSerializer
from apps.curso.models import Curso
from rest_framework.pagination import LimitOffsetPagination

class CursoViewSet(ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   GenericViewSet
):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    pagination_class = LimitOffsetPagination