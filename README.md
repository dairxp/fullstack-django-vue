# Vue Django Fullstack App

Aplicación Fullstack moderna combinando Django y Vue.js con autenticación JWT

## Stack Tecnológico

### Backend

- **Django** - Framework web Python
- **Django REST Framework** - API REST
- **JWT** - Autenticación con tokens
- **Serializers** - Validación y transformación de datos

### Frontend

- **Vue ** - Framework JavaScript reactivo
- **Pinia** - State management
- **Axios** - Cliente HTTP

## Requisitos

- Python
- uv
- Node.js
- pnpm

## Instalación

### Backend (uv)

```bash
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

### Frontend

```bash
cd frontend
pnpm install
pnpm run dev
```
