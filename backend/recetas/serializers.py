from rest_framework import serializers
from .models import *

class RecetaSerializer(serializers.ModelSerializer):

    #categoria = serializers.ReadOnlyField(source='categorias.nombre')
    categoria = serializers.CharField(source='categorias.nombre')
    fecha=serializers.DateTimeField(format="%d/%m/%Y") #13/10/2026

    class Meta:
        model = Receta
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categorias_id")

