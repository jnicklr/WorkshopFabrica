from rest_framework import serializers
from apps.curso.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nome', 'mensalidade', 'tempo_conclusao', 'conteudo']
