from rest_framework import serializers
from .models import *

class RecetaSerilalizer(serializers.ModelSerializer):

    class Meta:
        model = Receta
        fields = ('__all__')
