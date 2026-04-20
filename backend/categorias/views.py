from rest_framework.views import APIView
from .models import Categoria
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import CategoriaSerilalizer
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

class Clase1(APIView):

    def get(self, request):
        # Select * from categorias orden by id desc
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerilalizer(data, many=True)
        #return Response(datos_json.data)
        return JsonResponse({"data":datos_json.data}, status=HTTPStatus.OK)

    def post(self, request):
        if request.data.get("nombre") ==None or not request.data['nombre']:
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        try:
            Categoria.objects.create(nombre=request.data['nombre'])
            return JsonResponse({"estado":"ok", "mensaje": "Se crea el registro existosamente"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
    
class Clase2(APIView):

    def get(self, request, id):
        # Select *from categroais where id=4
        try:
            data = Categoria.objects.filter(id=id).get()
            #data = Categoria.objects.filter(id=id).first()
            return JsonResponse({"data": {"id": data.id, "nombre": data.nombre, "slug": data.slug}}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404

    def put(self, request, id):
        if request.data.get("nombre") == None:
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        if not request.data.get("nombre"):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).update(nombre=request.data.get("nombre"), slug=slugify(request.data.get("nombre")))
            return JsonResponse({"estado":"ok", "mensaje": "Se modifico el registro existosamente"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
    
    def delete(self,  request, id):
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).delete()
            return JsonResponse({"estado":"ok", "mensaje": "Se elimino el registro existosamente"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404