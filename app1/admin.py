from django.contrib import admin
from app1.models import Employee

# Register your models here.

class employee_admin(admin.ModelAdmin):
    emp_dict = ['emp_no','emp_name','emp_salary','emp_address']

    


admin.site.register(Employee,employee_admin)
