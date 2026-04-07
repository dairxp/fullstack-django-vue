from django.urls import path
from .views import *

urlpatterns = [
    path('ejemplo', Class_Ejemplo.as_view()),
    path('ejemplo/<int:id>', Class_EjemploParamentro.as_view())
]
