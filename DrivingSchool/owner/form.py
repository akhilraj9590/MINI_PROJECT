from dataclasses import fields
from tkinter import Widget
from django import forms
from user.models import Instructor

class addInstructors(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'