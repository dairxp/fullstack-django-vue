from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.contrib.auth.models import User
import uuid

from .models import *

class Clase1(APIView):
    def post(self,request):
        if request.data.get("nombre")==None or not request.data.get("nombre"):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("correo")==None or not request.data.get("correo"):
            return JsonResponse({"estado":"error", "mensaje":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("password")==None or not request.data.get("password"):
            return JsonResponse({"estado":"error", "mensaje":"El campo password es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if User.objects.filter(email=request.data["correo"]).exists():
            return JsonResponse({"estado":"error", "mensaje": f"El coore {request.data["correo"]} no esta disponible"}, status=HTTPStatus.BAD_REQUEST)
