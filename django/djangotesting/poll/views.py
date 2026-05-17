from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. controlador -> vista, vista -> plantilla
# en views manejamos los controladores

def index(request):
    return HttpResponse('Hello world, hello mum')

def overview(request):
    return HttpResponse('Here is a list of the general functions of the app:')
# VA A RETORNAR UN TEXTO HELLO WORLD PERO EN HTML
# ENRUTADOR
# Enrutar esto, asignar la funcion a una ruta /polls /encuestas