from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse,Http404
#from rest_framework.response import Response
from http import HTTPStatus
#upload
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

# Create your views here.
class Class_Ejemplo(APIView):
    
    def get(self, request): #Listar registro
        #return HttpResponse("Metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}")
        #return Response({"estado":"OK", "mensaje": f"Metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}"})
        return JsonResponse({"estado":"OK", "mensaje": f"Metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}"}, status=HTTPStatus.OK) #estatus=200

    def post(self, request): #Listar registro
        if request.data.get("correo") == None or request.data.get("password") == None:
            raise Http404
        # return HttpResponse("Metodo POST")
        return JsonResponse({"estado": "OK", "mensaje": f"Metodo POST | correo={request.data.get('correo')} | password={request.data.get('password')}"}, status=HTTPStatus.CREATED) #status=201

class Class_EjemploParamentro(APIView):

    def get(self, request, id): #Listar registro
        return HttpResponse(f"Metodo GET | parametro={id}")
    
    def put(self, request, id):
        return HttpResponse(f"Metodo PUT | parametro={id}")
    
    def delete(self, request, id):
        return HttpResponse(f"Metodo DELETE | parametro={id}")
    
class Class_EjemploUpload(APIView):
    
    def post(self, request):
        fs = FileSystemStorage()
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
        fs.save(f"ejemplo/{foto}", request.FILES['file'])
        fs.url(request.FILES['file'])
        return JsonResponse({"estado": "OK", "mensaje":"Se subio el archivo"})