from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import CustomerDetails ,ServiceApplication,User


class Resistrationform(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['CustomerId','BranchId','DrivingPackage','FirstName' , 'LastName','Gender','Phone1','Phone2','BranchId']

class ApplyNewLicenceform(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['CustomerId','BranchId','ServiceName','SSLC','IdProof','Photo','PhysicalFitness','AgeProof']

        # Widget {
        #     CustomerId : 
        # }
        # def __init__(self, *args, **kwargs):
        #     self.request = kwargs.pop("request")
        #     super(ApplyNewLicenceform, self).__init__(*args, **kwargs)
        #     self.fields["CustomerId"].queryset = User.objects.get(username=self.request.user)
       

        

        