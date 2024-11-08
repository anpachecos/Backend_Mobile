from rest_framework import generics
from .models import Carrera, Jornada, Estudiante, Profesor, Asignatura, Seccion, Sala, AsignaturaSeccion, InscripcionEstudiante, HorarioClase, EstadoAsistencia, RegistroAsistencia
from .serializers import (CarreraSerializer, JornadaSerializer, EstudianteSerializer, ProfesorSerializer, 
                          AsignaturaSerializer, SeccionSerializer, SalaSerializer, AsignaturaSeccionSerializer, 
                          InscripcionEstudianteSerializer, HorarioClaseSerializer, EstadoAsistenciaSerializer, 
                          RegistroAsistenciaSerializer)

class CarreraListCreate(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class JornadaListCreate(generics.ListCreateAPIView):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer

class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class ProfesorListCreate(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class AsignaturaListCreate(generics.ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class SeccionListCreate(generics.ListCreateAPIView):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class SalaListCreate(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class AsignaturaSeccionListCreate(generics.ListCreateAPIView):
    queryset = AsignaturaSeccion.objects.all()
    serializer_class = AsignaturaSeccionSerializer

class InscripcionEstudianteListCreate(generics.ListCreateAPIView):
    queryset = InscripcionEstudiante.objects.all()
    serializer_class = InscripcionEstudianteSerializer

class HorarioClaseListCreate(generics.ListCreateAPIView):
    queryset = HorarioClase.objects.all()
    serializer_class = HorarioClaseSerializer

class EstadoAsistenciaListCreate(generics.ListCreateAPIView):
    queryset = EstadoAsistencia.objects.all()
    serializer_class = EstadoAsistenciaSerializer

class RegistroAsistenciaListCreate(generics.ListCreateAPIView):
    queryset = RegistroAsistencia.objects.all()
    serializer_class = RegistroAsistenciaSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer