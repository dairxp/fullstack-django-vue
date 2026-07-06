from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404, HttpResponseRedirect
from http import HTTPStatus
from django.contrib.auth.models import User
import uuid
import os
from dotenv import load_dotenv

from .models import *
from utilidades import utilidades

class Clase1(APIView):
    def post(self,request):
        if request.data.get("nombre")==None or not request.data.get("nombre"):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("correo")==None or not request.data.get("correo"):
            return JsonResponse({"estado":"error", "mensaje":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if request.data.get("password")==None or not request.data.get("password"):
            return JsonResponse({"estado":"error", "mensaje":"El campo password es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if User.objects.filter(email=request.data["correo"]).exists():
            return JsonResponse({"estado":"error", "mensaje": f"El correo {request.data["correo"]} no esta disponible"}, status=HTTPStatus.BAD_REQUEST)


        token = uuid.uuid4()
        url = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}"
        try:
            u = User.objects.create_user(username=request.data["correo"], password=request.data["password"], email=request.data["correo"], first_name=request.data["nombre"], last_name="", is_active=False)

            UserMetadata.objects.create(token=token, user_id=u.id)

            html= f"""

                <h3>Verificacion de cuenta</h3>
                Hola {request.data["nombre"]} te has registrado exitosamente. Para activar tu cuenta haz click en el siguiente enlace: <br/>
                <a href="{url}">{url}</a>
            """
            utilidades.sendMail(html, "Verificación", request.data["correo"])

        except Exception as e:
            print(f"Error al registrar: {e}") # Para poder ver el error real en tu consola
            return JsonResponse({"estado":"error", "mensaje": "Ocurrio un error inesperado"}, status=HTTPStatus.BAD_REQUEST)

        return JsonResponse({"estado":"ok", "mensaje": "Se crea el registro exitoso"}, status=HTTPStatus.CREATED)


class Clase2(APIView):

    def get(self, request, token):
        if token== None or not token:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, status=404)
        try:
            data=UserMetadata.objects.filter(token=token).get()
            UserMetadata.objects.filter(token=token).update(token="")
            User.objects.filter(id=data.user_id).update(is_active=1)

            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTEND"))

        except UserMetadata.DoesNotExist:
            raise Http404
