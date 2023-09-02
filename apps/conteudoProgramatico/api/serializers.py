from rest_framework import serializers
from apps.conteudoProgramatico.models import ConteudoProgramatico

class ConteudoProgramaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoProgramatico
        fields = ['area_do_conteudo', 'periodo', 'carga_horaria', 'materias']
