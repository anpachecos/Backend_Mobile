from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario, Asignatura, HorarioAsignatura, Asistencia
from .serializers import UsuarioSerializer, AsignaturaSerializer, HorarioAsignaturaSerializer, AsistenciaSerializer



@api_view(['GET'])
def get_user_by_name(request):
    """
    Endpoint para buscar un usuario por su nombre.
    """
    nombre = request.query_params.get('search', None)  # Obtiene el parámetro 'search' de la URL
    if nombre:
        try:
            usuario = Usuario.objects.get(nombre=nombre)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Falta el parámetro de búsqueda'}, status=status.HTTP_400_BAD_REQUEST)

















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
