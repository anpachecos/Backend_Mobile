from rest_framework import serializers
from .models import Usuario, Asignatura, HorarioAsignatura, Asistencia

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class HorarioAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioAsignatura
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'
