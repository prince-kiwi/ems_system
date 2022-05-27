import email
from django.shortcuts import render,redirect
from .forms import Employee_Registration_Forms,CheckIn_Forms,CheckOut_Forms
from .models import Employee_Registration,CheckIn, logdetails
from django.http import HttpResponseRedirect
from datetime import datetime,date,time
from django.contrib import messages
# Create your views here.
# def home(request):
#     return render(request,'home.html')


def Registration(request):
    if request.method == 'POST':
        fm =Employee_Registration_Forms(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            fn = fm.cleaned_data['father_name']
            mn = fm.cleaned_data['mother_name']
            gen = fm.cleaned_data['gender']
            em = fm.cleaned_data['email']
            mob = fm.cleaned_data['mobile_no']
            add = fm.cleaned_data['address']
            dob = fm.cleaned_data['dob']
            reg = Employee_Registration(name=n,father_name=fn,mother_name=mn,gender=gen,email=em,mobile_no=mob,address=add,dob=dob)
            print(reg)
            reg.save()
            messages.success(request,'Registration Successfully !!')
            print("sucess")
            return HttpResponseRedirect('/')
    else:
        fm = Employee_Registration_Forms()        
    return render(request,'registrations.html',{'form':fm})


def CheckinView(request):
    form=CheckIn_Forms
    if request.method=="POST":
        form=CheckIn_Forms(request.POST)
        if form.is_valid():
            em=form.cleaned_data['email']
            user = Employee_Registration.objects.get(email__exact=em)
            if user.status is False:
                form.save()
                user.status=True
                user.save()
                print("sucess")
                messages.success(request,'Check In Successfully !!')
                return HttpResponseRedirect('/')

            else:
                messages.success(request,'You Have already Checkin please Checkout !!')
                return HttpResponseRedirect('/checkout')

        else:
            form = CheckIn_Forms()
    return render(request,'check_in.html',{'form':form})

def CheckoutView(request):

    if request.method == 'POST':
        form = CheckOut_Forms(request.POST)
        if form.is_valid():
            em=form.cleaned_data['email']
            user = Employee_Registration.objects.get(email__exact=em)
            if user.status is True:
                td=date.today()
                log = logdetails.objects.get(email=em,log_date=td,check_out=None)
                log.check_out=datetime.now().time()
                print(log)
                log.save()
                user.status=False
                user.save()
                messages.success(request,'Check Out Successfully !!')
                return HttpResponseRedirect('/')
            else:
                messages.success(request,'You Have already Checkout please Checkin !!')
                return HttpResponseRedirect('/checkin')
    else:
        form = CheckOut_Forms()
    return render(request,'check_out.html',{'form':form})

