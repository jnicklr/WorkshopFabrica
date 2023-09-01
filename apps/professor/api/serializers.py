from rest_framework import serializers
from apps.professor.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['nome', 'area_atuacao', 'valor_hora']
