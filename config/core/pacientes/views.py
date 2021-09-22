from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.pacientes.models import *
# Create your views here.
class PacientesListView(ListView):
    model = Patients
    template_name = 'pacientes.html'
