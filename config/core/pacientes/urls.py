from django.urls import path

from core.pacientes.views import *

urlpatterns = [
    path('core/pacientes',PacientesListView.as_view() , name='pacientes'),

]
