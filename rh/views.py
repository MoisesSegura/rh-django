from django.shortcuts import render

from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'rh/employee_list.html', {'employees': employees})