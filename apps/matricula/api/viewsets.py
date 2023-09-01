from rest_framework.viewsets import ModelViewSet
from .serializers import MatriculaSerializer
from apps.matricula.models import Matricula
from rest_framework.pagination import LimitOffsetPagination

class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    pagination_class = LimitOffsetPagination