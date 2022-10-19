from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile 
from customer.models import *

# Create your views here.
@login_required
def index(request):
    return render(request,'staff/index.html')

@login_required
def AppliedServices(request):
    s1 = request.user
    br = Profile.objects.get(user_id=s1).staffBranch_id
    services = ServiceApplication.objects.filter(BranchId_id = br)
    
    context = {
        'services':services,
        'br' : br ,
    }
    return render(request,'staff/appliedServices.html',context)

@login_required
def studentDetails(request):
    # students = CustomerDetails.objects.all()
    # context = {
    #     'students' : students , 
    # }
    return render (request,'staff/studentDetails.html',context)