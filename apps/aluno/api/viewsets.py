from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import AlunoSerializer
from apps.aluno.models import Aluno
from rest_framework.pagination import LimitOffsetPagination

class AlunoViewSet(ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   GenericViewSet
):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    pagination_class = LimitOffsetPagination