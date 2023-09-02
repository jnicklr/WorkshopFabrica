# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.materia.models import Materia

# Criação do Serializer!
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ['id', 'nome', 'descricao', 'assunto', 'professor', 'carga_horaria']
