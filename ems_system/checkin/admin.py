from django.contrib import admin
from .models import Employee_Registration,logdetails

# Register your models here.
@admin.register(Employee_Registration)
class Employee_Registration(admin.ModelAdmin):
    list_display = ['id','date','name', 'father_name','mother_name','email','mobile_no','dob','address','status']

@admin.register(logdetails)
class logdetails(admin.ModelAdmin):
    list_display = ['id','email','log_date','check_in','check_out','mod_trans']