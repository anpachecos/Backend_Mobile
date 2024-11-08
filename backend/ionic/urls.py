from django.urls import path
from .views import (CarreraListCreate, JornadaListCreate, EstudianteListCreate, EstudianteDetail, ProfesorListCreate,
                    AsignaturaListCreate, SeccionListCreate, SalaListCreate, AsignaturaSeccionListCreate,
                    InscripcionEstudianteListCreate, HorarioClaseListCreate, EstadoAsistenciaListCreate,
                    RegistroAsistenciaListCreate)

urlpatterns = [
    path('carreras/', CarreraListCreate.as_view(), name='carrera-list-create'),
    path('jornadas/', JornadaListCreate.as_view(), name='jornada-list-create'),
    path('estudiantes/', EstudianteListCreate.as_view(), name='estudiante-list-create'),
    path('estudiantes/<int:pk>/', EstudianteDetail.as_view(), name='estudiante-detail'),
    path('profesores/', ProfesorListCreate.as_view(), name='profesor-list-create'),
    path('asignaturas/', AsignaturaListCreate.as_view(), name='asignatura-list-create'),
    path('secciones/', SeccionListCreate.as_view(), name='seccion-list-create'),
    path('salas/', SalaListCreate.as_view(), name='sala-list-create'),
    path('asignatura_secciones/', AsignaturaSeccionListCreate.as_view(), name='asignatura_seccion-list-create'),
    path('inscripciones/', InscripcionEstudianteListCreate.as_view(), name='inscripcion-list-create'),
    path('horarios_clase/', HorarioClaseListCreate.as_view(), name='horario_clase-list-create'),
    path('estado_asistencias/', EstadoAsistenciaListCreate.as_view(), name='estado_asistencia-list-create'),
    path('registro_asistencias/', RegistroAsistenciaListCreate.as_view(), name='registro_asistencia-list-create'),
]
