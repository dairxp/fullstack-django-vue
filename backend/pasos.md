### crear backen desde misma carpeta

    django-admin startproject config .

### crerar app

    django-admin startapp home

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
