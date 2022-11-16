from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
MaleOrFemale = (
    ( 'male' , 'male'),
    ( 'female','female' )
)


class Branch(models.Model):
    BranchName =  models.CharField(max_length=100,null=True)
    def __str__(self):
        return f'{self.BranchName}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    staffBranch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True,blank =True)

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class ServicesNameAndPrice(models.Model):
    ServiceName = models.CharField(max_length=100,null=True)
    amount = models.PositiveBigIntegerField(null=True)
    def __str__(self):
        return f'{self.ServiceName}-{self.amount}'

class studyLicenceNameAndPrice(models.Model):
    LicenceType = models.CharField(max_length=100,null=True)
    amount = models.PositiveBigIntegerField(null=True)
    def __str__(self):
        return f'{self.LicenceType}---Rs:{self.amount}'


class Instructor(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Branch =models.ForeignKey(Branch, on_delete=models.CASCADE, null=True,blank =True)
    Age = models.PositiveBigIntegerField(null=True)
    Gender = models.CharField(max_length=100,null=True,choices=MaleOrFemale)
    Experience = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f'{self.Name}'


class RcModificationsAndPrice(models.Model):
    ServiceName = models.CharField(max_length=100,null=True)
    amount = models.PositiveBigIntegerField(null=True)
    def __str__(self):
        return f'{self.ServiceName}---Rs:{self.amount}'


class LicenceModificationsAndPrice(models.Model):
    ServiceName = models.CharField(max_length=100,null=True)
    amount = models.PositiveBigIntegerField(null=True)
    def __str__(self):
        return f'{self.ServiceName}---Rs:{self.amount}'




    

