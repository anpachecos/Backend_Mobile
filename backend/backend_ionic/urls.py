from django.urls import path
from .views import (
    UsuarioListCreate, AsignaturaListCreate, HorarioAsignaturaListCreate,
    AsistenciaListCreate, get_user_by_name, add_asistencia, get_asistencias_usuario
)
from .views import update_usuario, update_password

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuarios/search/', get_user_by_name, name='get-user-by-name'),  # Nueva ruta para buscar por nombre
    path('asignaturas/', AsignaturaListCreate.as_view(), name='asignatura-list-create'),
    path('horarios/', HorarioAsignaturaListCreate.as_view(), name='horario-list-create'),
    path('asistencias/', AsistenciaListCreate.as_view(), name='asistencia-list-create'),
    path('usuarios/<int:pk>/', update_usuario, name='update_usuario'),
    path('usuarios/update-password/', update_password, name='update-password'),
    path('asistencias/', add_asistencia, name='add-asistencia'),
    path('asistencias/<int:usuario_id>/', get_asistencias_usuario, name='get-asistencias-usuario'),

]
