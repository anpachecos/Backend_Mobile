from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario, Asignatura, HorarioAsignatura, Asistencia
from .serializers import UsuarioSerializer, AsignaturaSerializer, HorarioAsignaturaSerializer, AsistenciaSerializer

@api_view(['GET', 'PUT', 'DELETE'])  # Incluye GET aquí
def update_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)

    serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)  # Retorna los datos actualizados
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_user_by_name(request):
    nombre = request.query_params.get('search')  # Usar el parámetro 'search' para buscar
    if not nombre:
        return Response({'error': 'Falta el parámetro search'}, status=400)
    try:
        usuario = Usuario.objects.get(nombre=nombre)
        # Puedes devolver solo el ID o el objeto completo
        return Response({'id': usuario.id, 'nombre': usuario.nombre, 'apellido': usuario.apellido})
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)
    
@api_view(['PUT'])
def update_password(request):
    """
    Endpoint para actualizar la contraseña de un usuario
    """
    nombre = request.data.get('nombre')
    new_password = request.data.get('new_password')

    if not nombre or not new_password:
        return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(nombre=nombre)
        usuario.contrasena = new_password  # Actualiza la contraseña
        usuario.save()  # Guarda los cambios en la base de datos
        return Response({'message': 'Contraseña actualizada correctamente'}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_asistencia(request):
    """
    Endpoint para registrar una asistencia
    """
    usuario_id = request.data.get('usuario')
    nombre = request.data.get('nombre')
    seccion = request.data.get('seccion')
    sala = request.data.get('sala')
    fecha = request.data.get('fecha')
    estado = request.data.get('estado')

    if not (usuario_id and nombre and seccion and sala and fecha and estado):
        return Response(
            {'error': 'Faltan datos obligatorios.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        asistencia = Asistencia.objects.create(
            usuario=usuario,
            nombre=nombre,
            seccion=seccion,
            sala=sala,
            fecha=fecha,
            estado=estado
        )
        return Response(
            {'message': 'Asistencia registrada correctamente.'},
            status=status.HTTP_201_CREATED
        )
    except Usuario.DoesNotExist:
        return Response(
            {'error': 'Usuario no encontrado.'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def get_asistencias_usuario(request, usuario_id):
    """
    Endpoint para obtener asistencias de un usuario.
    """
    try:
        asistencias = Asistencia.objects.filter(usuario_id=usuario_id)
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Asistencia.DoesNotExist:
        return Response({"error": "No se encontraron asistencias para este usuario."}, status=status.HTTP_404_NOT_FOUND)














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
