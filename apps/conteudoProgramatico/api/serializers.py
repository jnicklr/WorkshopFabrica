# Bibliotecas e Models necessários para o serializer!
from rest_framework import serializers
from apps.conteudoProgramatico.models import ConteudoProgramatico

# Criação do Serializer!
class ConteudoProgramaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoProgramatico
        fields = ['area_do_conteudo', 'periodo', 'carga_horaria', 'materias']
