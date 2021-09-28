from django.urls import path
from core.employee.views import *

urlpatterns = [
    path('empleado/lista/', employeeList, name='employee_list')
]