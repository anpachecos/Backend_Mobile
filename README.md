# Sistema de Gestión de Usuarios y Asistencias

Este proyecto es un backend desarrollado con Django que gestiona usuarios, asignaturas, horarios y registros de asistencia para mi app "Mis Asistencias Duoc" -> https://github.com/anpachecos/Mi-Asistencia-Duoc

---

## Funcionalidades

1. **Usuarios**:
   - Registro de usuarios con nombre, apellido, correo electrónico y contraseña.
   - Actualización de contraseñas mediante un endpoint dedicado.

2. **Asignaturas**:
   - Registro de asignaturas con su nombre, sección, sala, días de clase y horarios.

3. **Horarios de Asignaturas**:
   - Gestión de horarios específicos para las asignaturas.
   - Control de fechas de inicio y fin, días de la semana, y horas de clase.

4. **Asistencias**:
   - Registro de asistencias de los estudiantes basado en un código QR que contiene información de la clase (asignatura, sección, sala, y fecha).

---

## Endpoints Disponibles

1. **Gestión de Usuarios**
   - `GET /api/usuarios/`: Obtiene una lista de usuarios.
   - `PUT /api/usuarios/update-password/`: Actualiza la contraseña de un usuario.

2. **Gestión de Asignaturas**
   - `GET /api/asignaturas/`: Obtiene una lista de asignaturas.
   - `POST /api/asignaturas/`: Crea una nueva asignatura.

3. **Gestión de Horarios**
   - `GET /api/horarios/`: Obtiene una lista de horarios.

4. **Gestión de Asistencias**
   - `POST /api/asistencias/`: Registra la asistencia de un estudiante.
