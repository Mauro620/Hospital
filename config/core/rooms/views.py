from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.rooms.models import *
# Create your views here.
class RoomsListView(ListView):
    model = rooms
    template_name = 'salas.html'