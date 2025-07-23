from django.shortcuts import render
from app1.models import Employee

# Create your views here.

def get_data(request):
    emp_data = Employee.objects.all()
    emp_dict = {'emp_list':emp_data}

    return render(request,'result.html',context=emp_dict)




