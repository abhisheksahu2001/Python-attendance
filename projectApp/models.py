from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    enrollNo = models.CharField(max_length=50,blank=True)
    date_time = models.CharField(max_length=20, null=True)
    Attendance = models.BooleanField(blank=True, null=True)