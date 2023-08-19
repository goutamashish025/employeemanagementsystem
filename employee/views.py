from django.shortcuts import render, HttpResponse , get_object_or_404
from . models import Department,Employee, Role, Details,Project,Event
from datetime import datetime
from django.db.models import Q 
import random


# Create your views here.
def index(request):
    emps = Employee.objects.all()
    project_data = Project.objects.all()
    events = Event.objects.all()
    context = {
        'emps': emps,
        'project_data' : project_data,
        'events' : events,
    }
    # print(context)
    
    # projs = Project.objects.all()
    # proj_data = {
    #     'projs':projs
    # }
    # print(proj_data)
    return render(request, 'index.html',context)

def dashboard(request):
    return render(request, 'dashboard.html')

def employee(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'employee.html',context)

def attendance(request):
    return render(request, 'attendance.html')

def payroll(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    
    
    return render(request, 'payroll.html',context)

def setting(request):
    return render(request, 'setting.html')

def logout(request):
    return render(request, 'logout.html')

def add_employee(request):
    if request.method == 'POST':
        id = random.randint(1000, 10000)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = int(request.POST['phone'])
        dob = request.POST['dob']
        email = request.POST['email']
        # dept = request.POST['dept']
        dept = Department.objects.get(name=request.POST['dept'])  # Retrieve the Department instance
        # employee.dept = dept  # Assign the Department instance
        role = Role.objects.get(name=request.POST['role'])
        yoe = int(request.POST['yoe'])
        salary = int(request.POST['salary'])
        new_emp = Employee(first_name= first_name, last_name=last_name,id = id, phone = phone,dob = dob,email = email ,dept = dept,role = role , hire_date =  datetime.now(), yoe = yoe , salary=salary )
        new_emp.save()
        
        return render(request,'index.html')
    elif request.method=='GET':
        return render(request, 'addemp.html')
    
    
def delete_employee(request,id):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    if id:
        emp_removed = Employee.objects.get(id=id)
        emp_removed.delete()
        return HttpResponse('Employee deleted successfully')

def update_employee(request,id):
    emp = get_object_or_404(Employee, id=id)
    # emps = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'update_employee.html', {'emp': emp})

def updatedetails(request,id):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = int(request.POST['phone'])
        dob = request.POST['dob']
        email = request.POST['email']
        # dept = request.POST['dept']
        dept = Department.objects.get(name=request.POST['dept'])  # Retrieve the Department instance
        # employee.dept = dept  # Assign the Department instance
        role = Role.objects.get(name=request.POST['role'])
        yoe = int(request.POST['yoe'])
        salary = int(request.POST['salary'])
        new_emp = Employee(first_name= first_name, last_name=last_name,id = id, phone = phone,dob = dob,email = email ,dept = dept,role = role , hire_date =  datetime.now(), yoe = yoe , salary=salary )
        new_emp.save()

        
        return render(request,'index.html')
        