# Atributos do ViewSet:
from .serializers import AlunoSerializer
from apps.aluno.models import Aluno

# Método para definir a paginação no ViewSet:
from rest_framework.pagination import LimitOffsetPagination

# Bibliotecas necessárias para a criação dos ViewSets
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# O ViewSet possui todas as operações de um CRUD: 
# GET, POST, PUT/PATCH e DELETE.
# Foi optado pela utilização dos mixins para caso fosse necessário fazer alguma manipulação nos dados!
# Também poderia ter sido utilizado o ModelViewSet que faria tudo automaticamente assim como eles! 

class AlunoViewSet(ListModelMixin, # LIST
                   CreateModelMixin, # POST
                   RetrieveModelMixin, # GET
                   UpdateModelMixin, # PUT
                   DestroyModelMixin, # DELETE
                   GenericViewSet # Definir ViewSet
):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    pagination_class = LimitOffsetPagination