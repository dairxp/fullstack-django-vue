from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo(APIView):
    def get(self, request): #Listar registro
        return HttpResponse("Metodo GET")
    
    def post(self, request): #Listar registro
        return HttpResponse("Metodo POST")
    

class Class_EjemploParamentro(APIView):
    def get(self, request, id): #Listar registro
        return HttpResponse(f"Metodo GET | parametro={id}")
    
    def put(self, request, id):
        return HttpResponse(f"Metodo PUT | parametro={id}")
    
    def delete(self, request, id):
        return HttpResponse(f"Metodo DELETE | parametro={id}")