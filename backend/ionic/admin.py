from django.contrib import admin
from .models import Carrera, Jornada, Estudiante, Profesor, Asignatura, Seccion, Sala, AsignaturaSeccion, InscripcionEstudiante, HorarioClase, EstadoAsistencia, RegistroAsistencia

admin.site.register(Carrera)
admin.site.register(Jornada)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Seccion)
admin.site.register(Sala)
admin.site.register(AsignaturaSeccion)
admin.site.register(InscripcionEstudiante)
admin.site.register(HorarioClase)
admin.site.register(EstadoAsistencia)
admin.site.register(RegistroAsistencia)
