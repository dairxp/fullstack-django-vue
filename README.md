# Vue Django Fullstack App

Aplicación Fullstack moderna combinando Django y Vue.js con autenticación JWT

## Stack Tecnológico

### Backend

- **Django** - Framework web Python
- **Django REST Framework** - API REST
- **JWT** - Autenticación con tokens
- **Serializers** - Validación y transformación de datos

### Frontend

- **Vue 3** - Framework JavaScript reactivo
- **Pinia** - State management
- **Axios** - Cliente HTTP

## Requisitos

- Python 3.8+
- uv
- Node.js 16+
- pnpm

## Instalación

### Backend (uv)

```bash
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver

uv run manage.py runserver
```

### Frontend

```bash
cd frontend
pnpm install
pnpm run dev
```
