from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.CharField(max_length=5)
    sala = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} - Sección {self.seccion} - Sala {self.sala}"

class HorarioAsignatura(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    dia_semana = models.CharField(
        max_length=10,
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ]
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha_inicio = models.DateField()  # Rango de fechas
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.dia_semana} de {self.fecha_inicio} a {self.fecha_fin}"

class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha = models.DateField()  # Fecha específica de la clase
    estado = models.CharField(
        max_length=10,
        choices=[
            ('asistió', 'Asistió'),
            ('faltó', 'Faltó')
        ]
    )

    def __str__(self):
        return f"{self.usuario.nombre} - {self.asignatura.nombre} - {self.estado} - {self.fecha}"
