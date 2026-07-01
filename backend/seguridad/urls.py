from django.urls import path
from .views import *

urlpatterns = [
    path('seguridad/registro', Clase1.as_view()),
]
