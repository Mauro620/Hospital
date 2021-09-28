from django.urls import path
from core.patients.views import *

urlpatterns = [
    path('pacientes/', PacientesListView.as_view(), name='pacientes'),

]
