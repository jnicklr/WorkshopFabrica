# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.curso.models import Curso

# Criação do Serializer!
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'mensalidade', 'tempo_conclusao', 'conteudo']
