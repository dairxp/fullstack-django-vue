from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_inicio(request):
    return HttpResponse("<h2>Hola desde django</h2>")