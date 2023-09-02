# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.aluno.models import Aluno

# Criação do Serializer!
class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'identidade', 'cpf', 'data_nascimento']
