from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employees/history/<int:employee_id>/', views.employee_history, name='employee_history'),
    path('', RedirectView.as_view(url='/accounts/login/')),
]