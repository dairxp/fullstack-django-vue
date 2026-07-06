#from functools import _NOT_FOUND
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from .serializers import RecetaSerializer
from .models import Receta, Categoria
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from seguridad.decorators import logueado
# Agrega esta línea para que BASE_URL funcione
load_dotenv()

# Create your views here.
class Clase1(APIView):

    def get(self, request):
        data =Receta.objects.order_by('-id').all()
        datos_json= RecetaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data})

    @logueado()
    def post(self, request):
        if request.data.get("nombre")==None or not request.data["nombre"]:
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatoria"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("tiempo")==None or not request.data["tiempo"]:
            return JsonResponse({"estado":"error", "mensaje":"El campo tiempo es obligatoria"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("descripcion")==None or not request.data["descripcion"]:
            return JsonResponse({"estado":"error", "mensaje":"El campo descripcion es obligatoria"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("categoria_id")==None or not request.data["categoria_id"]:
            return JsonResponse({"estado":"error", "mensaje":"El campo categoria_id es obligatoria"}, status=HTTPStatus.BAD_REQUEST)

        #validar no exista la categoriID
        try:
            #categoria =Categoria.objects.filter(pk=request.data["categoria_id"].get())
            categoria = Categoria.objects.get(pk=request.data.get("categoria_id"))
        except Categoria.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"La categoria_id no existe en al base de datos"}, status=HTTPStatus.BAD_REQUEST)
        # En lugar de try/except, usamos un simple IF
        # if not Categoria.objects.filter(pk=request.data.get("categoria_id")).exists():
        #     return JsonResponse({"estado":"error", "mensaje":"La categoria_id no existe"}, status=HTTPStatus.BAD_REQUEST)

        #select *from recetas where nombre=request.data.get("nombre")
        #validamos nombre de receta este disponible
        if Receta.objects.filter(nombre=request.data.get("nombre")).exists():
            return JsonResponse({"estado":"error", "mensaje":f"El nombre {request.data['nombre']} no esta disponible"}, status=HTTPStatus.BAD_REQUEST)

        fs =FileSystemStorage()
        try:
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Debe adjuntar una foto para la receta"}, status=HTTPStatus.BAD_REQUEST)

        print(request.FILES["foto"].content_type)
        if request.FILES["foto"].content_type=="image/jpeg" or request.FILES["foto"].content_type=="image/png":
            try:
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url(request.FILES['foto'])
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"Se produjo un error al subir un archivo"}, status=HTTPStatus.BAD_REQUEST)

            try:
                Receta.objects.create(nombre=request.data["nombre"], tiempo=request.data.get("tiempo"), descripcion=request.data["descripcion"], categorias_id=request.data.get("categoria_id"), fecha=datetime.now(), foto=foto)

                ### Receta.objects.create(nombre=request.data["nombre"], tiempo=request.data.get("tiempo"), descripcion=request.data["descripcion"], categorias_id=request.data.get("categoria_id"), fecha=datetime.now(), foto="SSS")
                return JsonResponse({"estado":"OK", "mensaje": "Se crea el registro existosamente"}, status=HTTPStatus.CREATED)
            except Exception as e:
                raise Http404

        return JsonResponse({"estado":"error", "mensaje":"La foto solo puede ser png y jng"})


class Clase2(APIView):

    def get(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
            return JsonResponse({"data":{"id":data.id,"nombre":data.nombre, "slug":data.slug, "tiempo":data.tiempo, "descripcion":data.descripcion, "fecha":DateFormat(data.fecha).format('d/m/Y'), "categoria_id":data.categorias_id, "categoria":data.categorias.nombre, "imagen":f"{os.getenv('BASE_URL')}uploads/recetas/{data.foto}"}}, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Recursos no disponible"}, status=HTTPStatus.NOT_FOUND)

    @logueado()
    def put(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
        except Receta.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recursos no disponible"}, status=HTTPStatus.NOT_FOUND)


        # 2. Validaciones de campos obligatorios
        # Usamos una lista para no repetir tantos 'if' y que el código sea más limpio

        # if request.data.get("nombre")==None or not request.data["nombre"]:
        #     return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatoria"}, status=HTTPStatus.BAD_REQUEST)
        # if request.data.get("tiempo")==None or not request.data["tiempo"]:
        #     return JsonResponse({"estado":"error", "mensaje":"El campo tiempo es obligatoria"}, status=HTTPStatus.BAD_REQUEST)

        campos_obligatorios = ["nombre", "tiempo", "descripcion", "categoria_id"]
        for campo in campos_obligatorios:
            if not request.data.get(campo):
                return JsonResponse({"estado":"error", "mensaje":f"El campo {campo} es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        try:
            categoria = Categoria.objects.get(pk=request.data.get("categoria_id"))
        except Categoria.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"La categoria_id no existe en al base de datos"}, status=HTTPStatus.BAD_REQUEST)

        # Actualización
        try:
            Receta.objects.filter(pk=id).update(
                nombre=request.data["nombre"],
                slug=slugify(request.data["nombre"]),
                tiempo=request.data.get("tiempo"),
                descripcion=request.data["descripcion"],
                categorias_id=request.data.get("categoria_id")
            )
            return JsonResponse({"estado":"ok", "mensaje":"Se modifico el registro"}, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"ocurrio un error"}, status=HTTPStatus.NOT_FOUND)

    @logueado()
    def delete(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
        except Receta.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recursos no disponible"}, status=HTTPStatus.NOT_FOUND)

        #borrar la foto de la carpeta
        os.remove(f"./uploads/recetas/{data.foto}")
        # En lugar
        # ruta = f"uploads/recetas/{data.foto}"
        # if os.path.exists(ruta):
        #     os.remove(ruta)

        #borrar el registor de la BD
        Receta.objects.filter(id=id).delete()
        return JsonResponse({"estado":"ok", "mensaje":"Se elimina el registro existosamente"}, status=HTTPStatus.OK)
