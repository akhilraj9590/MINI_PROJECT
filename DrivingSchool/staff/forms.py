from dataclasses import fields
from tkinter import Widget
from django import forms
from customer.models import *

class DateInput(forms.DateInput):
    input_type = 'date'
class AppliedServicesform(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['Status']

class AppliedRCServicesform(forms.ModelForm):
    class Meta:
        model = ServiceApplicationOfRcModification
        fields = ['Status']

class AppliedLicenceServicesform(forms.ModelForm):
    class Meta:
        model = ServiceApplicationOfLicenceModification
        fields = ['Status']

class TestLearningDatesForm(forms.ModelForm):
    class Meta:
        model = ServiceApplication
        fields = ['learnigdate','leanigStatus','testDate','testStatus']
        widgets = {
            'learnigdate': DateInput(),
            'testDate': DateInput()
        }