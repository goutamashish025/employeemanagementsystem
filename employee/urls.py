from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employee', views.employee, name='employee'),
    path('attendance', views.attendance, name='attandance'),
    path('payroll', views.payroll, name='payroll'),
    path('setting', views.setting, name='setting'),
    path('logout', views.logout, name='logout'),
    path('add', views.add_employee, name='add'),
    path('updatedetails', views.updatedetails, name='updatedetails'),
    path('delete/<int:id>', views.delete_employee, name='delete'),
    path('update/<int:id>', views.update_employee, name='update'),
]