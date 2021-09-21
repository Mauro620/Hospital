from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Inicio(request):
    return render(request, 'index.html')

def pacientes(request):
    return render(request, 'pacientes.html' )

def empleados(request):
    return render(request, 'Empleados.html' )

def salas(request):
    return render(request, 'salas.html' )

def principal(request):
    return render(request, 'principal.html' )