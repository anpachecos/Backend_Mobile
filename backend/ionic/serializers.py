from rest_framework import serializers
from .models import Carrera, Jornada, Estudiante, Profesor, Asignatura, Seccion, Sala, AsignaturaSeccion, InscripcionEstudiante, HorarioClase, EstadoAsistencia, RegistroAsistencia

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class AsignaturaSeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignaturaSeccion
        fields = '__all__'

class InscripcionEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscripcionEstudiante
        fields = '__all__'

class HorarioClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioClase
        fields = '__all__'

class EstadoAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoAsistencia
        fields = '__all__'

class RegistroAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAsistencia
        fields = '__all__'
