from rest_framework import serializers
from .models import *
from dotenv import load_dotenv
import os
from django.conf import settings

class RecetaSerializer(serializers.ModelSerializer):

    categoria = serializers.ReadOnlyField(source='categorias.nombre')
    #categoria = serializers.CharField(source='categorias.nombre')
    fecha=serializers.DateTimeField(format="%d/%m/%Y") #13/10/2026
    imagen = serializers.SerializerMethodField()


    class Meta:
        model = Receta
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categorias_id", "imagen")


    def get_imagen(self, obj):
        #return f"Hola {obj.id}"
        return f"{os.getenv('BASE_URL')}uploads/recetas/{obj.foto}"
