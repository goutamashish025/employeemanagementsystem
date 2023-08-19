from django.contrib import admin
from .models import Employee, Department, Role,Background, Emp_salary, Project, Event

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)
# admin.site.register(Details)
admin.site.register(Background)
admin.site.register(Emp_salary)
admin.site.register(Project)
admin.site.register(Event)
