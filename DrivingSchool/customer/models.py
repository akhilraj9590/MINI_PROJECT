from distutils.command.upload import upload
from django.db import models
from user.models import Branch,ServicesNameAndPrice,studyLicenceNameAndPrice
from user.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date,time


MaleOrFemale = (
    ( 'male' , 'male'),
    ( 'female','female' )
)

serviceProgresses = (
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Forwarded to RTO','Forwarded to RTO'),
    ('Complete','Complete')
)
scheduleStatus = (
    ( 'Up Coming' , 'Up Coming'),
    ( 'Complete','Complete' )
)
    
class CustomerDetails(models.Model):
    CustomerId = models.ForeignKey(User,on_delete=models.CASCADE)
    BranchId =  models.ForeignKey(Branch, on_delete=models.CASCADE)  
    DrivingPackage = models.ForeignKey(studyLicenceNameAndPrice,on_delete=models.CASCADE, null=True, db_constraint=False)  
    FirstName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=250,null=True)
    DateOfBirth = models.DateField(null=True)
    Gender = models.CharField(max_length=20,choices=MaleOrFemale,null=True)
    Phone1 = models.CharField(max_length=100,null=True)
    Phone2 = models.CharField(max_length=100,null=True)
    TotalHours = models.FloatField(null=True,default=10)
    CompletedHours = models.FloatField(default=0)
    CreatedTime = models.TimeField(default=timezone.now)
    CreatedDate = models.DateField(default=date.today )
    def __str__(self):
        return f'{self.FirstName} {self.LastName}'

class DrivingStudyDetails(models.Model):
    DrivingCustomer = models.ForeignKey(CustomerDetails,on_delete=models.CASCADE)
    # BranchId =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    # package = models.CharField(max_length=100,null=True)
    # amount = models.PositiveBigIntegerField(null=True)
    TotalHours = models.FloatField(null=True)
    CompletedHours = models.FloatField(default=0)

    def __str__(self):
        return f'{self.CustomerId.FirstName} {self.CustomerId.LastName}-{self.BranchId.BranchName}-{self.package}'


class SavedLicence(models.Model): #already have licence or save licence after got it
    CustomerId = models.ForeignKey(User,on_delete=models.CASCADE)
    LicenceType = models.CharField(max_length=30,null=True) #please make sure that all type of storred licence type
    LicenceNumber = models.CharField(max_length=40,null=True) #may change it to image field 

    def __str__(self):
        return f'{self.CustomerId.FirstName}-{self.LicenceType}-{self.LicenceNumber}'

testStatus = (
    ( 'Not Scheduled' , 'Not Scheduled'),
    ('Scheduled','Scheduled'),
    ( 'Complete','Complete')
)

class ServiceApplication(models.Model):
    CustomerId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_constraint=False)
    BranchId =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    ServiceName = models.ForeignKey(ServicesNameAndPrice, on_delete=models.CASCADE,null=True)
    SSLC = models.ImageField(upload_to = "ssleImages",null = True,blank=True)
    IdProof = models.ImageField(upload_to = "IdProof",null = True,blank=True)
    Photo = models.ImageField(upload_to = "Photo",null = True,blank=True)
    PhysicalFitness =models.ImageField(upload_to = "PhysicalFitness",null = True,blank=True)
    AgeProof = models.ImageField(upload_to = "AgeProof",null = True,blank=True)
    VehicleRegistration = models.ImageField(upload_to = "RCbook",null = True,blank=True)
    ApplicationOfPSV = models.ImageField(upload_to = "PSVapplication",null = True,blank=True)
    MedicalCirtifict = models.ImageField(upload_to = "MedicalCirtifict",null = True,blank=True)
    SchoolCirtifict = models.ImageField(upload_to = "SchoolCirtifict",null = True,blank=True)
    DrivingLicenseOld = models.ImageField(upload_to = "DrivinLicenseOld",null = True,blank=True)
    Status = models.CharField(max_length=100,null = True,choices=serviceProgresses,default="Pending")
    learnigdate = models.DateField(null = True,blank=True)
    testDate = models.DateField(null = True,blank=True)
    leanigStatus = models.CharField(max_length=100,null = True,blank=True,choices=testStatus,default="Not Scheduled")
    testStatus = models.CharField(max_length=100,null = True,blank=True,choices=testStatus,default="Not Scheduled")
    time = models.TimeField(default=timezone.now,null=True)
    Date = models.DateField(default=date.today,null=True)

    def __str__(self):
        return f'{self.CustomerId}-{self.ServiceName}'

class schedule(models.Model):
    drivingApplication = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, null = True, db_constraint=False)
    # customer =  models.ForeignKey(CustomerDetails, on_delete=models.CASCADE,null=True,blank=True)
    timeInHour = models.IntegerField(null=True,blank=True)
    Venue = models.CharField(max_length =100,null=True)
    Date = models.DateField()
    time = models.TimeField()
    Status = models.CharField(max_length=20,choices=scheduleStatus,null=True,default="Up Coming")
    def __str__(self):
        return f'{self.drivingApplication.id}'



class Payment(models.Model):
    CustomerId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_constraint=False)
    BranchId =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(null=True)
    time = models.TimeField(default=timezone.now)
    Date = models.DateField(default=date.today )
    discription = models.CharField(max_length =200,null=True)
    # driveRelated = models.BooleanField(null=True,default=False)
    def __str__(self):
        return f'{self.CustomerId}-Rs:{self.amount}-(Date : {self.Date}) '
        #need dervice name

class AppliedServiceSchedule(models.Model):
    serviceId = models.OneToOneField(ServiceApplication,on_delete=models.CASCADE)
    learningDate = models.DateField(null=True,default=False)
    serviceDate = models.DateField(null=True,default=False)



class balanceAndAdvance(models.Model):
    CustomerId = models.OneToOneField(User, on_delete=models.CASCADE, null=True, db_constraint=False)
    total = models.PositiveIntegerField(null=True,default=0)
    paid = models.PositiveIntegerField(null=True,default=0)



