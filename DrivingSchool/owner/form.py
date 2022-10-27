from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from user.models import Instructor
from django.contrib.auth.models import User


class addInstructors(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

# class addStaffForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','password']