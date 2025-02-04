# 1️⃣ Activa el entorno virtual
.\venv\Scripts\activate

# ⚠️ Si no funciona el comando anterior, intenta con:
.\venv\Scripts\Activate.ps1

# 2️⃣ Aplica las migraciones para actualizar la base de datos
python manage.py makemigrations
python manage.py migrate

# 3️⃣ Crea un superusuario para acceder al panel de administración (si aún no lo hiciste)
python manage.py createsuperuser

# 4️⃣ Inicia el servidor para ejecutar la página web en tu servidor local
python manage.py runserver

# Proyecto Hotel Luna

Este es un proyecto de un sistema de gestión de reservas de un hotel desarrollado con Django.

## 🏨 Funcionalidades del Proyecto "Hotel Luna"
Este sistema permite gestionar un hotel con 12 habitaciones, integrando funcionalidades de reservas online, gestión administrativa, disponibilidad por temporadas, blog de noticias y una sección de búsqueda laboral.

🔹 Gestión de Habitaciones
Función: Crear, modificar y eliminar habitaciones desde el panel de administración.

El sistema cuenta con 12 habitaciones distribuidas en diferentes categorías:

4 Dobles Estándar
4 Dobles Superiores
2 Individuales Estándar
2 Individuales Superiores
Desde la sección de administración se pueden gestionar los datos de cada habitación:

Tipo de habitación
Número de habitación
Disponibilidad (por temporada)
🔹 Sistema de Reservas (Online y Administración)
Función: Permite que los clientes hagan reservas online y que el administrador gestione reservas manualmente desde el panel.

Reservas Online: Los clientes pueden seleccionar fechas de entrada y salida, y confirmar su reserva si hay disponibilidad.
Reservas Manuales: Desde el panel de administración, los empleados pueden cargar reservas realizadas por teléfono o en persona.

El administrador puede hacer reservar de forma presencial o telefónica

Cada reserva incluye:

Usuario/Cliente
Tipo de habitación reservada
Fecha de entrada y salida
Estado de la reserva (Confirmada, Pendiente, Cancelada)
🔹 Cancelación y Modificación de Reservas
Función: Permite al usuario cancelar o modificar una reserva desde la sección de administración o desde el sistema online.

Cancelación de Reserva: Cambia el estado de la reserva a "Cancelada".
Modificación de Reserva: El administrador puede editar los detalles de una reserva existente, como fechas o tipo de habitación.
Nota: El sistema verifica que las habitaciones estén disponibles antes de confirmar cualquier modificación.

🔹 Visualización de Disponibilidad por Temporada
Función: Muestra las habitaciones disponibles según la temporada seleccionada (Verano o Invierno).

El cliente o el administrador puede ver:

Habitaciones disponibles para una fecha específica.
Temporada a la que pertenece la habitación (Verano/Invierno).
Esto permite optimizar la gestión del hotel y evitar errores de sobre-reserva.

🔹 Sección de Búsqueda Laboral
Función: El hotel puede publicar ofertas laborales disponibles.

Desde la sección "Búsqueda Laboral", los administradores pueden:

Publicar nuevos puestos de trabajo.
Editar o eliminar ofertas existentes.
Cada oferta laboral incluye:

Puesto de trabajo
Descripción del puesto
Salario estimado
Fecha de publicación
Los usuarios del sitio pueden visualizar las ofertas disponibles y postularse directamente.

🔹 Blog de Noticias del Hotel
Función: Permite al hotel publicar noticias o novedades relevantes.

Desde el blog, el administrador puede:

Publicar noticias relacionadas con eventos del hotel, promociones, etc.
Editar y eliminar publicaciones existentes.
Cada publicación del blog incluye:

Título del artículo
Cuerpo del artículo
Fecha de publicación
El blog mejora la interacción del hotel con sus clientes, manteniéndolos informados sobre novedades.


## 🛠️ Tecnologías utilizadas
- Python 3.11
- Django 5.1.4
- HTML, CSS, Bootstrap
- SQLite (base de datos por defecto)

## ⚙️ Configuración del entorno
1. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv.\venv\Scripts\activate
PS C:\Proyecto Hotel> .\venv\Scripts\Activate.ps1
>> 
(venv) PS C:\Proyecto Hotel> cd "C:\Proyecto Hotel\hotel_luna"

📋 Rutas de Navegación del Panel de Administración

Aquí tiene todas las rutas principales del sistema, tanto las páginas públicas como las del panel de administración de Django, donde puedes gestionar habitaciones, reservas, usuarios y más.
Navegación de la web.

 Entrar primero por administración y luego boton ir al sitio.
 
 
🔒 Panel de Administración de Django
Función	Ruta de Navegación	Descripción
Panel de Administración	http://127.0.0.1:8000/admin/	Página principal del panel de administración.
Habitaciones	http://127.0.0.1:8000/admin/reservas/habitacion/	Gestión de habitaciones del hotel.
Reservas	http://127.0.0.1:8000/admin/reservas/reserva/	Gestión de reservas realizadas.
Búsqueda Laboral	http://127.0.0.1:8000/admin/reservas/busquedalaboral/	Gestión de ofertas laborales del hotel.
Usuarios	http://127.0.0.1:8000/admin/auth/user/	Gestión de usuarios registrados.
Grupos	http://127.0.0.1:8000/admin/auth/group/	Gestión de grupos de permisos.

Usuario Administrativo
Usuario benit
Contraseña Benit123

Página	URL
Página principal	http://127.0.0.1:8000/
Temporada de verano	http://127.0.0.1:8000/verano/
Temporada de invierno	http://127.0.0.1:8000/invierno/
Disponibilidad	http://127.0.0.1:8000/disponibilidad/
Reserva online	http://127.0.0.1:8000/reserva_online/
Listado de reservas	http://127.0.0.1:8000/listado_reservas/
Blog	http://127.0.0.1:8000/blog/
Iniciar sesión	http://127.0.0.1:8000/usuarios/login/
Registro de usuarios	http://127.0.0.1:8000/usuarios/registro/

Se cuenta con los siguientes usuarios online
unic 
pepe123 
## 📹 Video de Demostración

El video de demostración del proyecto se encuentra disponible en el repositorio:

- [Ver video de demostración](00-26-49.mp4)


En Conclusión este sistema está diseñado para facilitar la gestión de un hotel tanto desde el lado del cliente como desde la administración interna. Combina la gestión de habitaciones, reservas online, disponibilidad, y funcionalidades adicionales como un blog y ofertas laborales. 🚀