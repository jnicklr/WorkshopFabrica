from rest_framework.viewsets import ModelViewSet
from .serializers import MateriaSerializer
from apps.materia.models import Materia
from rest_framework.pagination import LimitOffsetPagination

class MateriaViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    pagination_class = LimitOffsetPagination