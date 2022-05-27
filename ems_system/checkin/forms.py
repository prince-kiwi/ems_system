from django import forms
from .models import Employee_Registration,CheckIn,CheckOut,logdetails

class Employee_Registration_Forms(forms.ModelForm):
    class Meta:
        model = Employee_Registration
        #fields= '__all__'
        exclude = ['date','status']
        #fields = ['username','name','father_name','mother_name','gender','email','mobile_no','country_name','state','city','zipcode','address','vehicle_type','vehicle','vehicle_company','vehicle_model','vehicle_number','date']
         

class CheckIn_Forms(forms.ModelForm):
    class Meta:
        model = logdetails
        exclude = ['check_out','log_date']

class CheckOut_Forms(forms.ModelForm):
    class Meta:
        model = logdetails
        exclude = ['check_in','log_date','mod_trans','check_out']


#class Logdetails_Forms(forms.ModelForm):
 #   class Meta:
  #      model = logdetails
   #     fields = ['username','checkout_date','checkout_time']


