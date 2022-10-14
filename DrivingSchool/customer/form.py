from dataclasses import fields
from django import forms
from .models import CustomerDetails ,ServiceApplication

class Resistrationform(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['CustomerId','BranchId','FirstName' , 'LastName','Gender','Phone1','Phone2','BranchId']

class ApplyNewLicenceform(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['CustomerId','BranchId','ServiceName','SSLC','IdProof','Photo','PhysicalFitness','AgeProof']