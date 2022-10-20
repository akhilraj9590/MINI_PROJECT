from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile ,studyLicenceNameAndPrice , Instructor
from customer.models import CustomerDetails, ServiceApplication


# Create your views here.
@login_required
def index(request):
    return render(request,'owner/index.html')

@login_required
def staffDetails(request):
    staff1 = Profile.objects.filter(is_staff= True)
    context = {
        'staff1' : staff1,
    }
    return render (request,'owner/staffDetails.html',context)

@login_required
def studentDetails(request):
    student1 = CustomerDetails.objects.all()
    context = {
        'student1':student1,

    }
    return render (request,'owner/studentDetails.html',context)

@login_required
def appliedServices(request):
    services1 = ServiceApplication.objects.all()
    context = {
        'services1':services1
    }
    return render (request,'owner/appliedServices.html',context)

@login_required
def instructor(request):
    instructor1 = Instructor.objects.all()
    context = {
        'instructor1':instructor1,
    }
    return render (request,'owner/instructor.html',context)