from rest_framework import serializers
from apps.materia.models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ['nome', 'descricao', 'assunto', 'professor', 'carga_horaria']
