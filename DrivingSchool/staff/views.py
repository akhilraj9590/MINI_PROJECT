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
    # services = ServiceApplication.objects.filter(BranchId=)
    context = {
        'services': services
    }
    return render(request,'staff/appliedServices.html',context)