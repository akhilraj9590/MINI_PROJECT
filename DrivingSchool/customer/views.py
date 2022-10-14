import http
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import ApplyNewLicenceform, Resistrationform ,ServiceApplication
from user.models import Branch



# Create your views here.
@login_required
def index(request):
    return render(request,'customer/index.html')

@login_required
def admission(request):
    if request.method == 'POST':
        form = Resistrationform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Resistrationform()
    context = {
        "form" : form
    }
    return render(request,'customer/admission.html',context)

def selectBranch(request):
    branch = Branch.objects.all()
    context = {
        'branch' : branch ,
    }
    return render(request,'customer/selectBranch.html',context)

def applyNewLicence(request):
    if request.method == 'POST':
        form = ApplyNewLicenceform(request.POST,use_required_attribute=False)
        if form.is_valid():
            form.save()
    else:
        form = ApplyNewLicenceform()
    context = {
        "form" : form
    }
    return render(request , 'customer/applyNewLicence.html',context)

def appliedService(request):
    services = ServiceApplication.objects.all()
    context = {
        'services' : services,
    }
    return render(request,'customer/appliedService.html',context)