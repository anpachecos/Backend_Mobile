from django.urls import path
from .views import UsuarioListCreate, AsignaturaListCreate, HorarioAsignaturaListCreate, AsistenciaListCreate

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('asignaturas/', AsignaturaListCreate.as_view(), name='asignatura-list-create'),
    path('horarios/', HorarioAsignaturaListCreate.as_view(), name='horario-list-create'),
    path('asistencias/', AsistenciaListCreate.as_view(), name='asistencia-list-create'),
]
