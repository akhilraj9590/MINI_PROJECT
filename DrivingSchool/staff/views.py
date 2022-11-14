from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile 
from customer.models import *
from .forms import AppliedServicesform

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
    comp1 = ServiceApplication.objects.filter(Status="Complete").first()
    # print("sdf",comp1.Status)
    context = {
        'services':services,
        'br' : br ,
        'brName':brName,
        'comp1':comp1,
    }
    return render(request,'staff/manageAppliedServices.html',context)


@login_required
def update_services(request, pk):
    service1 = ServiceApplication.objects.get(id=pk)
    brName = Profile.objects.get(user=request.user).staffBranch

    if request.method == 'POST' :
        form = AppliedServicesform(request.POST,initial={'Status':service1.Status })
        service1.Status=form.data['Status']
        service1.save()
        return redirect("staff-ManageAppliedServices")
    else:
        form = AppliedServicesform(initial={'Status':service1.Status })

    context = {
        'service1' : service1 ,
        'form' : form,
        'brName':brName,
    }
    return render(request,'staff/update_services.html',context)

@login_required
def viewDocuments(request,pk):
    service1 = ServiceApplication.objects.get(id=pk)
    serviceName1 = ServiceApplication.objects.get(id=pk).ServiceName.ServiceName
    nameLMV = ServicesNameAndPrice.objects.get(ServiceName='LMV').ServiceName
    nameMC = ServicesNameAndPrice.objects.get(ServiceName='M/C').ServiceName
    nameHeavyBadge = ServicesNameAndPrice.objects.get(ServiceName='HEAVY + BADGE').ServiceName
    nameConductor = ServicesNameAndPrice.objects.get(ServiceName='CONDUCTOR').ServiceName
    nameHazardous  = ServicesNameAndPrice.objects.get(ServiceName='HAZARDOUS').ServiceName
    localHost1=request.get_host()
    # print("sdf", request.get_host())
    context = {
        'localHost1':localHost1,
        'service1':service1,
        'serviceName1':serviceName1,
        'nameLMV': nameLMV,
        'nameMC':nameMC,
        'nameHeavyBadge':nameHeavyBadge,
        'nameConductor':nameConductor,
        'nameHazardous':nameHazardous
    }
    return render(request,'staff/viewDocuments.html',context)
@login_required
def manageStudentSchedule(request):
    s1= request.user
    # staffBranch1 = Profile.objects.all()
    # studentScheduleAvailable2 = CustomerDetails.objects.all().values('CompletedHours')
    # studentScheduleAvailable1 = CustomerDetails.objects.all().values('TotalHours')
    # print(staffBranch1,"staff branch")
    # for each in staffBranch1:
    #     print(each.staffBranch)
    return render(request,'staff/ManageStudentSchedule.html')