from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile 
from customer.models import *
from .forms import AppliedServices

# Create your views here.
@login_required
def index(request):
    brName = Profile.objects.get(user=request.user).staffBranch
    context = {
        'brName':brName,
    }
    return render(request,'staff/index.html',context)

@login_required
def AppliedServices(request):
    s1 = request.user
    br = Profile.objects.get(user_id=s1).staffBranch_id
    brName = Profile.objects.get(user=request.user).staffBranch

    services = ServiceApplication.objects.filter(BranchId_id = br)
    
    context = {
        'services':services,
        'br' : br ,
        'brName':brName,
    }
    return render(request,'staff/appliedServices.html',context)

@login_required
def studentDetails(request):
    s1 = request.user
    br = Profile.objects.get(user_id=s1).staffBranch_id
    students = CustomerDetails.objects.filter(BranchId=br)
    brName = Profile.objects.get(user=request.user).staffBranch

    context = {
        'students' : students ,
         'brName':brName,
    }
    return render (request,'staff/studentDetails.html',context)

@login_required
def ManageAppliedServices(request):
    s1 = request.user
    br = Profile.objects.get(user_id=s1).staffBranch_id
    services = ServiceApplication.objects.filter(BranchId_id = br)
    brName = Profile.objects.get(user=request.user).staffBranch

    
    context = {
        'services':services,
        'br' : br ,
        'brName':brName,
    }
    return render(request,'staff/manageAppliedServices.html',context)


@login_required
def update_services(request, pk):
    service1 = ServiceApplication.objects.get(id=pk)
    brName = Profile.objects.get(user=request.user).staffBranch

    if request.method == 'POST' :
        form = AppliedServices(request.POST)
        service1.Status = 'hai'
        service1.save()
    else:
        form = AppliedServices

    context = {
        'service1' : service1 ,
        'form' : form,
        'brName':brName,
    }
    return render(request,'staff/update_services.html',context)

