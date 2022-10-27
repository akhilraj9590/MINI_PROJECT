from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile ,studyLicenceNameAndPrice , Instructor
from customer.models import CustomerDetails, ServiceApplication
from .form import addInstructors
from customer.form import Resistrationform
from django.contrib.auth.forms import UserCreationForm
from user.models import Branch



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

@login_required
def addInstructor(request):
    if request.method == 'POST':
        form = addInstructors(request.POST)
        if form.is_valid():
            form.save()
            return redirect (instructor)
    else:
        form = addInstructors()
    context = {
        "form" : form
    }
    return render(request,'owner/addInstructor.html',context)

@login_required
def addStaff(request):
    branchName = Branch.objects.all()
    if request.method == 'POST':
        branch1 = request.POST.get('stfBranch')
        branchid1 = Branch.objects.get(BranchName=branch1).id
        print("fg",branchid1)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            user1 =User.objects.get(username=form.data['username']).id
            profilupdate = Profile.objects.get(user=user1)
            profilupdate.is_customer = False
            profilupdate.is_staff=True
            profilupdate.staffBranch_id=branchid1
            profilupdate.save()
            # return redirect (instructor)
    else:
        form = UserCreationForm()
    context = {
        "form" : form,
        "branchName":branchName,
    }
    return render(request,'owner/addStaff.html',context)