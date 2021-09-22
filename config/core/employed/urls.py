from django.urls import path

from core.employed.views import *

urlpatterns = [
    path('empleado/', EmployedListView.as_view(), name='empleados'),
]
