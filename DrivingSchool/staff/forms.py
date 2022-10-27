from dataclasses import fields
from django import forms
from customer.models import ServiceApplication

class AppliedServicesform(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['Status']