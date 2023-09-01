from rest_framework import serializers
from apps.matricula.models import Matricula

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'data_matricula', 'valor', 'turma', 'aluno']
