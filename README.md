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
- uv (recomendado para el backend)
- Node.js 16+
- pnpm

## Instalación

### Backend (uv)
```bash
cd backend
uv venv .venv
source .venv/Scripts/activate   # Git Bash
# PowerShell: .\.venv\Scripts\activate
uv pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Instalar paquetes nuevos (dentro del entorno):**
```bash
uv pip install nombre_paquete
```

### Frontend
```bash
cd frontend
pnpm install
npm run dev
```

## Desarrollado por
DairXP