from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import ProfessorSerializer
from apps.professor.models import Professor
from rest_framework.pagination import LimitOffsetPagination

class ProfessorViewSet(ListModelMixin,
                       CreateModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       DestroyModelMixin,
                       GenericViewSet
):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    pagination_class = LimitOffsetPagination