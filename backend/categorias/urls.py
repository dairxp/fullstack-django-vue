from django.urls import path
from .views import *

urlpatterns = [
    path('categorias', Clase1.as_view())
]