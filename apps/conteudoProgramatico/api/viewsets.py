from rest_framework.viewsets import ModelViewSet
from .serializers import ConteudoProgramaticoSerializer
from apps.conteudoProgramatico.models import ConteudoProgramatico
from rest_framework.pagination import LimitOffsetPagination

class ConteudoProgramaticoViewSet(ModelViewSet):
    queryset = ConteudoProgramatico.objects.all()
    serializer_class = ConteudoProgramaticoSerializer
    pagination_class = LimitOffsetPagination