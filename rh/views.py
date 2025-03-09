from django.shortcuts import render
from .models import Employee, EmployeeHistory
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'rh/employee_list.html', {'employees': employees})


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'rh/add_employee.html', {'form': form})

@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'rh/edit_employee.html', {'form': form})

@login_required
def employee_history(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    history = EmployeeHistory.objects.filter(employee=employee)
    return render(request, 'rh/employee_history.html', {'employee': employee, 'history': history})