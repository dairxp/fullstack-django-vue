from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse
from http import HTTPStatus
from datetime import datetime

# Create your views here.

class Clase1(APIView):

    def post(self, request):
        if request.data.get("nombre") ==None or not request.data['nombre']:
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("correo") ==None or not request.data['correo']:
            return JsonResponse({"estado":"error", "mensaje":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("telefono") ==None or not request.data['telefono']:
            return JsonResponse({"estado":"error", "mensaje":"El campo telefono es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("mensaje") ==None or not request.data['mensaje']:
            return JsonResponse({"estado":"error", "mensaje":"El campo mensaje es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        try:
            Contacto.objects.create(
                nombre=request.data["nombre"],
                correo=request.data["correo"],
                telefono=request.data["telefono"],
                mensaje=request.data["mensaje"],
                fecha=datetime.now()
            )
            return JsonResponse({"estado":"ok", "mensaje": "Se crea el contacto"}, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje": "Ocurrio un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
