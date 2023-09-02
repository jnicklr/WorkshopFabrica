from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import MatriculaSerializer
from apps.matricula.models import Matricula
from rest_framework.pagination import LimitOffsetPagination

class MatriculaViewSet(ListModelMixin,
                       CreateModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       DestroyModelMixin,
                       GenericViewSet
):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    pagination_class = LimitOffsetPagination