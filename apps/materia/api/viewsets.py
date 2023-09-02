from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import MateriaSerializer
from apps.materia.models import Materia
from rest_framework.pagination import LimitOffsetPagination

class MateriaViewSet(ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet
):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    pagination_class = LimitOffsetPagination