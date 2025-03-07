from django.contrib import admin
from .models import Department, Role, Employee, EmployeeHistory

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(EmployeeHistory)