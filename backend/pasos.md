### crear backen desde misma carpeta

    django-admin startproject config .

### crerar app

    django-admin startapp home

### Backend (uv)

Usamos el gestor de dependencias moderno de `uv` (basado en `pyproject.toml`).

```bash
cd backend
uv sync  # Crea el entorno virtual e instala dependencias basadas en pyproject.toml / uv.lock
uv run python manage.py migrate
uv run python manage.py runserver
```

**Instalar paquetes nuevos:**

```bash
uv add nombre_paquete
```

_(Esto añadirá el paquete a `pyproject.toml`, actualizará `uv.lock` y lo instalará en el entorno)._

**Ejecutar comandos en el entorno de uv:**
Para ejecutar cualquier script o comando de django, antepón `uv run`:

```bash
uv run python manage.py makemigrations
uv run python manage.py createsuperuser
```

**para ver imagen**

```bash
http://127.0.0.1:8000/uploads/ejemplo/hola.jpeg
```
