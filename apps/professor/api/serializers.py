# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.professor.models import Professor

# Criação do Serializer!
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'area_atuacao', 'valor_hora']
