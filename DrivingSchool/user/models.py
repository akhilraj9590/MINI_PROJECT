from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
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




    

