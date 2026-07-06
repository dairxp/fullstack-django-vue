import os
import sys
import django

sys.path.append(r"F:\PROYECTO IDE\AAA Proyectos ALD\dxp-projects\vue-django-fullstack-app\backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

try:
    user = User.objects.get(email="ali7@gmail.com")
    print(f"User ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Is active: {user.is_active}")
    print(f"Check password '123456': {user.check_password('123456')}")
    
    auth = authenticate(username=user.username, password="123456")
    print(f"Authenticate result: {auth}")
except Exception as e:
    print(f"Error: {e}")
