from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile 
from customer.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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

@login_required
def recipts(request):
    s1= request.user
    branch1 = Profile.objects.filter(user=s1)
    for each in branch1:
        branchName = each.staffBranch
    recipts1 = Payment.objects.filter(BranchId=branchName)
    # print(recipts1)
    totalrecipt = 0
    for each in recipts1:
        totalrecipt=totalrecipt+each.amount
    context = {
        'recipts1':recipts1,
        'totalrecipt':totalrecipt,
    }
    return render(request,'staff/recipts.html',context)

def userRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('staff-userRegistered')
    else:
        form = UserCreationForm()
    context ={
        'form': form,
    }
    return render(request,'staff/createStudentLogin.html',context)
def userRegistered(request):
    return render (request,'staff/userCreatedPage.html')

def student_view(request,pk):
    students = CustomerDetails.objects.get(id=pk)
    context = { 
        'students' : students
    }
    return render(request,'staff/student_view.html',context)

def render_pdf_view(request,pk):
    students = CustomerDetails.objects.get(id=pk)
    template_path = 'staff/student_form.html'
    context = {
        'myvar': 'this is your template context',
        'students':students
        
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def updateLearningTestDates(request, pk):
    service1 = ServiceApplication.objects.get(id=pk)
    # brName = Profile.objects.get(user=request.user).staffBranch

    if request.method == 'POST' :
        form = TestLearningDatesForm(request.POST,initial={'learnigdate':service1.learnigdate,'leanigStatus':service1.leanigStatus,'testDate':service1.testDate,'testStatus':service1.testStatus })
        print(form.data['learnigdate'],"asdf")
        service1.learnigdate=form.data['learnigdate']
        service1.leanigStatus=form.data['leanigStatus']
        service1.testDate=form.data['testDate']
        service1.testStatus=form.data['testStatus']
        service1.save()
        return redirect("staff-ManageAppliedServices")
    else:
        form = TestLearningDatesForm(initial={'learnigdate':service1.learnigdate,'leanigStatus':service1.leanigStatus,'testDate':service1.testDate,'testStatus':service1.testStatus })

    context = {
        'service1' : service1 ,
        'form' : form,
    }
    return render(request,'staff/updateLearingTestDates.html',context)