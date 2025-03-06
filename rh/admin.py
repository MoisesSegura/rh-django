from django.contrib import admin

from django.contrib import admin
from .models import Department, Employee, Attendance, Vacation

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Vacation)