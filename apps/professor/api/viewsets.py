from rest_framework.viewsets import ModelViewSet
from .serializers import ProfessorSerializer
from apps.professor.models import Professor
from rest_framework.pagination import LimitOffsetPagination

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    pagination_class = LimitOffsetPagination