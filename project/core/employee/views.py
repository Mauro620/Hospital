from django.shortcuts import render
from django.views.generic import ListView
from core.employee.models import employee

# Create your views here.
#class EmployeeListView(ListView):
 #   model = employee
  #  template_name = 'empleado.html'

def employeeList(request):
    data = {
        'title': 'Listado de empleados',
        'empleados': employee.objects.all()
    }
    return render(request, 'employeeList.html', data)