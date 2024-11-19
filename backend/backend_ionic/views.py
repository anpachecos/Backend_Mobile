from rest_framework import generics
from .models import Usuario, Asignatura, HorarioAsignatura, Asistencia
from .serializers import UsuarioSerializer, AsignaturaSerializer, HorarioAsignaturaSerializer, AsistenciaSerializer

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AsignaturaListCreate(generics.ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class HorarioAsignaturaListCreate(generics.ListCreateAPIView):
    queryset = HorarioAsignatura.objects.all()
    serializer_class = HorarioAsignaturaSerializer

class AsistenciaListCreate(generics.ListCreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
