from dataclasses import field
from statistics import mode
from django import forms
from .models import Student

class StudentAttendance(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Attendance']
        
        exclude = ()