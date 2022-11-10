import http
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import * 
from user.models import Branch 
from .models import *



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
    totalAmountcalc = 0
    for each in servicelist1:
        totalAmountcalc=totalAmountcalc+each.ServiceName.amount
    paidlist1 = Payment.objects.filter(CustomerId_id=c1)
    totalPaid=0
    for each in paidlist1:
        totalPaid=totalPaid+each.amount

    # payCustomer = balanceAndAdvance.objects.filter(CustomerId_id=c1)
   
    
    # if c1 in Payment.CustomerId_id:
    #     print(Payment.CustomerId_id)
    # else:
    #     print(Payment.CustomerId_id)
    payments1 = Payment.objects.filter(CustomerId=c1,driveRelated=True) 
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