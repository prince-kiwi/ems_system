from xml.etree.ElementTree import TreeBuilder
from django.db import models

# Create your models here.
Modof_travelling = (
    ('Two Wheeler','Two Wheeler'),
    ('Four Wheeler','Four Wheeler'),
    ('Public Transport','Public Transport'),

)

GNDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

class Employee_Registration(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length =100)
    gender = models.CharField(choices=GNDER_CHOICES,max_length=50)
    email = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=12) 
    address = models.CharField(max_length=200)
    dob= models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.email

class logdetails(models.Model):
    email= models.ForeignKey(Employee_Registration, on_delete=models.CASCADE)
    log_date=models.DateField(auto_now_add=True)
    check_in=models.TimeField(auto_now_add=True)
    check_out=models.TimeField(null=True)
    trans_choice=(('Public Transport','Public Transport'),('Bike','Bike'),('Car','Car'))
    mod_trans=models.CharField(max_length=50, choices=trans_choice)
    

class CheckIn(models.Model):
    username = models.ForeignKey(Employee_Registration,on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkin_time = models.TimeField() 
    
    
class CheckOut(models.Model):
    username = models.ForeignKey(Employee_Registration,on_delete=models.CASCADE)
    checkout_date = models.DateField()
    checkout_time = models.TimeField()
   
