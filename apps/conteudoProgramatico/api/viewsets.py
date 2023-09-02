from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import ConteudoProgramaticoSerializer
from apps.conteudoProgramatico.models import ConteudoProgramatico
from rest_framework.pagination import LimitOffsetPagination

class ConteudoProgramaticoViewSet(ListModelMixin,
                                  CreateModelMixin,
                                  RetrieveModelMixin,
                                  UpdateModelMixin,
                                  DestroyModelMixin,
                                  GenericViewSet
):
    queryset = ConteudoProgramatico.objects.all()
    serializer_class = ConteudoProgramaticoSerializer
    pagination_class = LimitOffsetPagination