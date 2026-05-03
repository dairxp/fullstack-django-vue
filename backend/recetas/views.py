from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from .serializers import *
from .models import *

# Create your views here.
class Clase1(APIView):
    
    def get(self, request):
        data =Receta.objects.order_by('-id').all()
        datos_json= RecetaSerilalizer(data, many=True)
        return JsonResponse({"data":datos_json.data})
