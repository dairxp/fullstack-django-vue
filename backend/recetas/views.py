from functools import _NOT_FOUND
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from .serializers import *
from .models import *
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os
from datetime import datetime

# Create your views here.
class Clase1(APIView):

    def get(self, request):
        data =Receta.objects.order_by('-id').all()
        datos_json= RecetaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data})

    def post(self, request):
        if request.data.get("nombre") or not request.data["nombre"]:
            return JsonResponse({"estado":"error", "mensaje":"El campo es obligatoria"}, status=HTTPStatus.BAD_REQUEST)
        try:
            Receta.objects.create(nombre=request.data["nombre"], tiempo=request.data.get("tiempo"), descripcion=request.data["descripcion"], categorias_id=request.data.get("categoria_id"), fecha=datetime.now(), foto="SSS")

             ### Receta.objects.create(nombre=request.data["nombre"], tiempo=request.data.get("tiempo"), descripcion=request.data["descripcion"], categorias_id=request.data.get("categoria_id"), fecha=datetime.now(), foto="SSS")
            return JsonResponse({"estado":"OK", "mensaje": "Se crea el registro existosamente"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404

class Clase2(APIView):

    def get(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
            return JsonResponse({"data":{"id":data.id,"nombre":data.nombre, "slug":data.slug, "tiempo":data.tiempo, "descripcion":data.descripcion, "fecha":DateFormat(data.fecha).format('d/m/Y'), "categoria_id":data.categorias_id, "categoria":data.categorias.nombre, "imagen":f"{os.getenv('BASE_URL')}uploads/recetas/{data.foto}"}}, status=HTTPStatus.OK)

        except:
            return JsonResponse({"estado":"error", "mensaje":"Recursos no disponible"}, status=HTTPStatus.NOT_FOUND)
