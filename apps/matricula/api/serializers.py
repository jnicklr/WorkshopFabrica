# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.matricula.models import Matricula

# Criação do Serializer!
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'data_matricula', 'valor', 'turma', 'aluno', 'curso', 'custo']
