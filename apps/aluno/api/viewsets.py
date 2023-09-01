from rest_framework.viewsets import ModelViewSet
from .serializers import AlunoSerializer
from apps.aluno.models import Aluno
from rest_framework.pagination import LimitOffsetPagination

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    pagination_class = LimitOffsetPagination