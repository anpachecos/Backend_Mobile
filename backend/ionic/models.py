from django.db import models

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_carrera

class Jornada(models.Model):
    nombre_jornada = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_jornada

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_asignatura

class Seccion(models.Model):
    nombre_seccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_seccion

class Sala(models.Model):
    nombre_sala = models.CharField(max_length=100)
    piso_sala = models.IntegerField()

    def __str__(self):
        return self.nombre_sala

class AsignaturaSeccion(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()

    def __str__(self):
        return f"{self.asignatura} - {self.seccion}"

class InscripcionEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura_seccion = models.ForeignKey(AsignaturaSeccion, on_delete=models.CASCADE)

class HorarioClase(models.Model):
    asignatura_seccion = models.ForeignKey(AsignaturaSeccion, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

class EstadoAsistencia(models.Model):
    nombre_estado = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre_estado

class RegistroAsistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    horario_clase = models.ForeignKey(HorarioClase, on_delete=models.CASCADE)
    hora_asistencia = models.TimeField()
    estado = models.ForeignKey(EstadoAsistencia, on_delete=models.CASCADE)
