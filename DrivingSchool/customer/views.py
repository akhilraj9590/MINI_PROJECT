import http
from multiprocessing import context
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import * 
from user.models import Branch 
from .models import *
import datetime
from django.contrib import messages




# Create your views here.
@login_required
def index(request):
    return render(request,'customer/index.html')

@login_required
def admission(request):
    c1=request.user.id
    if request.method == 'POST':
        form = Resistrationform(request.POST,initial={'CustomerId': c1})
        print(form)
        if form.is_valid():
            form.save()
    else:
        form = Resistrationform(initial={'CustomerId': c1})
    context = {
        "form" : form
    }
    return render(request,'customer/admission.html',context)

# def selectBranch(request):
#     branch = Branch.objects.all()
#     context = {
#         'branch' : branch ,
#     }
#     return render(request,'customer/selectBranch.html',context)
@login_required
def applyNewLicence(request):
    c1=request.user.id
    if request.method == 'POST':
        form = ApplyNewLicenceform(request.POST,use_required_attribute=False,initial={'CustomerId': c1})
        if form.is_valid():
            form.save()
            return redirect ('customer-index')
            
    else:
        form = ApplyNewLicenceform(initial={'CustomerId': c1})
    context = {
        "form" : form
    }
    return render(request , 'customer/applyNewLicence.html',context)


@login_required
def appliedService(request):
    c1 = request.user.id
    services = ServiceApplication.objects.filter(CustomerId_id=c1)
    # servicesid1 = ServiceApplication.objects.get(CustomerId_id=c1).id
    # serviceSchedule1 = AppliedServiceSchedule.objects.filter(serviceId_id=servicesid1)
    context = {
        'services' : services,
        # 'serviceSchedule1':serviceSchedule1,
    }
    return render(request,'customer/appliedService.html',context)


@login_required
def DrivingPaymentHistory(request):
    c1 = request.user
    servicelist1=ServiceApplication.objects.filter(CustomerId_id=c1)
    Customerlist2=CustomerDetails.objects.filter(CustomerId_id=c1)
    totalAmountcalc = 0
    for each in servicelist1:
        totalAmountcalc=totalAmountcalc+each.ServiceName.amount
    for each in Customerlist2:
        print(each.DrivingPackage.amount)
        totalAmountcalc= totalAmountcalc +each.DrivingPackage.amount
    paidlist1 = Payment.objects.filter(CustomerId_id=c1)
    totalPaid=0
    for each in paidlist1:
        totalPaid=totalPaid+each.amount

    # payCustomer = balanceAndAdvance.objects.filter(CustomerId_id=c1)
   
    
    # if c1 in Payment.CustomerId_id:
    #     print(Payment.CustomerId_id)
    # else:
    #     print(Payment.CustomerId_id)
    payments1 = Payment.objects.filter(CustomerId=c1,) 
    zero = 0
    balanceAdvanceCalc = totalAmountcalc-totalPaid
    negbalanceAdvanceCalc = balanceAdvanceCalc*-1
    context = {
        'payments1':payments1,
        'totalAmountcalc':totalAmountcalc,
        'totalPaid':totalPaid,
        'zero':zero,
        'balanceAdvanceCalc':balanceAdvanceCalc,
        'negbalanceAdvanceCalc':negbalanceAdvanceCalc,
    }
    return render(request,'customer/DrivingPaymentHistory.html',context)

def schedules(request):
    c1 = request.user
    drivingCustomerId = CustomerDetails.objects.filter(CustomerId=c1).values_list('id', flat=True)
    schedule1 = schedule.objects.filter(drivingApplication__id__in=drivingCustomerId)
    completeStatus  = "Complete"
    customerPackage = CustomerDetails.objects.filter(CustomerId=c1)
    print(customerPackage)
    context = {
        'schedule1':schedule1,
        'completeStatus':completeStatus, 
        'customerPackage':customerPackage,
    }
    
    return render(request,'customer/schedule.html',context)

def attendence(request):
    today=datetime.date.today()
    # print(today,"hai")
    c1 = request.user
    drivingCustomerId = CustomerDetails.objects.filter(CustomerId=c1).values_list('id', flat=True)
    schedule1 = schedule.objects.filter(drivingApplication__id__in=drivingCustomerId)
    # for each in schedule1:
    #     print(each)
    context = {
        'schedule1':schedule1,
        'Complete': 'Complete',
    }
    return render(request,'customer/attendence.html',context)

def pay(request):
    c1 = request.user
    servicelist1=ServiceApplication.objects.filter(CustomerId_id=c1)
    Customerlist2=CustomerDetails.objects.filter(CustomerId_id=c1)
    totalAmountcalc = 0
    for each in servicelist1:
        totalAmountcalc=totalAmountcalc+each.ServiceName.amount
    for each in Customerlist2:
        totalAmountcalc= totalAmountcalc +each.DrivingPackage.amount
    paidlist1 = Payment.objects.filter(CustomerId_id=c1)
    totalPaid=0
    for each in paidlist1:
        totalPaid=totalPaid+each.amount
    if (totalAmountcalc-totalPaid>0):
        balance = totalAmountcalc - totalPaid
    else:
        balance = 0
    # branch1 = CustomerDetails.objects.get(CustomerId_id=c1.id)
    if request.method == 'POST':
        form = paymentForm(request.POST,initial={'CustomerId': c1})
        if form.is_valid():
            form.save()
            return redirect('customer-DriningPaymentHistory')
    else:
        form = paymentForm(initial={'CustomerId': c1,'amount':balance})
    context = {
        'form':form ,
    }
    return render(request,'customer/payCash.html',context)

def RcModication(request):
    c1=request.user.id
    # print(c1,"df")
    if request.method == 'POST':
        form = RcModificationForm(request.POST,use_required_attribute=False,initial={'CustomerId': c1})
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            
    else:
        form = RcModificationForm(initial={'CustomerId': c1})
    context = {
        "form" : form
    }
    return render(request,'customer/applyRcModification.html',context)

def appliedRcService(request):
    c1 = request.user.id
    services = ServiceApplicationOfRcModification.objects.filter(CustomerId_id=c1)
    context = {
        'services' : services,
    }
    return render(request,'customer/appliedRcService.html',context)

def applyLicenceModificationService(request):
    c1=request.user.id
    if request.method == 'POST':
        form = LicenceModificationForm(request.POST,use_required_attribute=False,initial={'CustomerId': c1})
        if form.is_valid():
            form.save()
            return redirect ('customer-index')
            
    else:
        form = LicenceModificationForm(initial={'CustomerId': c1})
    context = {
        "form" : form,
    }
    return render(request,'customer/applyLicenceModification.html',context)

def appliedLicenceModificationService(request):
    c1 = request.user.id
    services = ServiceApplicationOfLicenceModification.objects.filter(CustomerId_id=c1)
    context = {
        'services' : services,
    }
    return render(request,'customer/appliedLicenceModificationService.html',context)