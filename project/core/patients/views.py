from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.patients.models import *
# Create your views here.

class PacientesListView(ListView):
    model = patients
    template_name = 'PatientList.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Listado de pacientes'
        return contex