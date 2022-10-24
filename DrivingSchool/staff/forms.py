from dataclasses import fields
from django import forms
from customer.models import ServiceApplication

class AppliedServices(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['CustomerId','BranchId','ServiceName','Status']