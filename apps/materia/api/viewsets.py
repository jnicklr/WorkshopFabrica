# Atributos do ViewSet:
from .serializers import MateriaSerializer
from apps.materia.models import Materia

# Método para definir a paginação no ViewSet:
from rest_framework.pagination import LimitOffsetPagination

# Bibliotecas necessárias para a criação dos ViewSets
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# O ViewSet possui todas as operações de um CRUD: 
# GET, POST, PUT/PATCH e DELETE.
# Foi optado pela utilização dos mixins para caso fosse necessário fazer alguma manipulação nos dados!
# Também poderia ter sido utilizado o ModelViewSet que faria tudo automaticamente assim como eles! 

class MateriaViewSet(ListModelMixin, # LIST (Pega múltiplos objetos)
                     CreateModelMixin, # POST
                     RetrieveModelMixin, # GET (Pega um único objeto pelo id)
                     UpdateModelMixin, # PUT
                     DestroyModelMixin, # DELETE
                     GenericViewSet # Definir ViewSet
):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    pagination_class = LimitOffsetPagination