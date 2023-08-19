from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=13,default="")
    email = models.EmailField(max_length=25,default="abc@gmail.com")
    id = models.CharField(max_length=10, primary_key=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    hire_date = models.DateField(null=False)
    yoe = models.CharField(max_length=10, null= False)
    salary = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)
    
    
class Details(models.Model):
    name = models.OneToOneField(Employee,on_delete=models.CASCADE,unique=True)
    # name = models.ForeignKey(Employee,on_delete=models.CASCADE,unique=True)
    present = models.CharField(max_length=10,null=True)
    leave = models.CharField(max_length=10,null=True)
    bonus=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return "%s" %(self.name)
    
class Background(models.Model):
    name = models.OneToOneField(Employee,on_delete=models.CASCADE,unique=True)
    # name = models.ForeignKey(Employee,on_delete=models.CASCADE,unique=True)
    dob = models.DateField(null=False)
    Aadhar_no = models.CharField(max_length=20,null=False)
    PAN = models.CharField(max_length=20,null=False)
    degree = models.CharField(max_length=20,null=False)
    diploma = models.CharField(max_length=20,null=False)
    class10 = models.CharField(max_length=20,null=False)
    class12 = models.CharField(max_length=20,null=False)
    skills = models.CharField(max_length=50,null=False)
    def __str__(self):
        return "%s" %(self.name)
    
class Emp_salary(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    attendance = models.CharField(max_length=20,null=False,default="0")
    present = models.CharField(max_length=20,null=False,default="0")
    leave = models.CharField(max_length=20,null=False,default="0")
    latecoming = models.CharField(max_length=20,null=False,default="0")
    halfday = models.CharField(max_length=20,null=False,default="0")
    month = models.CharField(max_length=20,null=False,default="0")
    def __str__(self):
        return "%s" %(self.name)
    
    
class Project(models.Model):
    project_name = models.CharField(max_length=100,null="false")
    technology = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name
    
class Event(models.Model):
    event_name = models.CharField(max_length=30,null=False)
    event_date = models.DateField(null=False)
    def __str__(self):
        return self.event_name
        
    
    
    
    
