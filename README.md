# JardinApp

JardinApp es un sistema web para gestionar solicitudes de visitas de jardinería. Permite que los clientes registren solicitudes, la empresa asigne jardineros, y se gestionen citas que pueden ser confirmadas, canceladas o calificadas por los usuarios.

## Requisitos

- Python 3.9+
- Django 5.2
- SQLite
- pip

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ignaciovillela/jardin-app.git
cd jardin-app
```

2. Crear entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/macOS
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py migrate
```

5. Crear un superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```

---


# Funcionalidades
- Registro de clientes como usuarios
- Solicitud de servicios con ubicación opcional (Leaflet.js)
- Asignación de jardineros por parte del administrador
- Confirmación, cancelación y calificación de citas por parte del cliente
- Vista de citas asignadas para administrador y cliente
- Gestión de jardineros desde panel admin

# Geolocalización
Se utiliza Leaflet.js para mostrar mapas. No requiere clave de API.

