from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.employed.models import employed

# Create your views here.
class EmployedListView(ListView):
    model = employed
    template_name = 'Empleados.html'
