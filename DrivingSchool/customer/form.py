from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import *




class DateInput(forms.DateInput):
    input_type = 'date'
class Resistrationform(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['CustomerId','BranchId','DrivingPackage','FirstName' , 'LastName','DateOfBirth','address','Gender','address','Phone1','Phone2','BranchId']
        widgets = {
            'DateOfBirth':DateInput(),
            'Phone1':forms.NumberInput(attrs={'maxlength':10,'minlength':10}),

            'Phone2':forms.NumberInput(attrs={'maxlength':10,'minlength':10})
        }


class ApplyNewLicenceform(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['CustomerId','BranchId','ServiceName','SSLC','IdProof','Photo','PhysicalFitness','AgeProof']

        # Widget = {
        #     'CustomerId': forms.TextInput(attrs={'required':True}),
        #     'SSLC': forms.ImageField(attrs={'required':True}),
        # }
        #     CustomerId : 
        # }
        # def __init__(self, *args, **kwargs):
        #     self.request = kwargs.pop("request")
        #     super(ApplyNewLicenceform, self).__init__(*args, **kwargs)
        #     self.fields["CustomerId"].queryset = User.objects.get(username=self.request.user)
class paymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

class RcModificationForm(forms.ModelForm):
    class Meta:
        model = ServiceApplicationOfRcModification
        fields = ['CustomerId','BranchId','ServiceName','VehicleRegistration','IdProof']

class LicenceModificationForm(forms.ModelForm):
    class Meta:
        model = ServiceApplicationOfLicenceModification
        fields = ['CustomerId','BranchId','ServiceName','IdProof','AgeProof']

        

        