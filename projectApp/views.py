from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .resources import StudentResource
from tablib import Dataset
from .models import Student
from .attendance import  StudentAttendance
from projectApp import attendance
import json

def home(request):
     form = StudentAttendance()
     students = Student.objects.all()
     context = {"form":form, "students":students}
     return render(request, 'input.html', context )


def export(request):
    Student_resource = StudentResource()
    dataset = Student_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="myclass.xls"'
    return response

@csrf_exempt
def save_attend(request):
        id = request.POST.get("id")
        attend = request.POST["attend"]
        try:
            if id is not None:
                student = Student.objects.get(id=str(id))
                student.Attendance = attend
                student.save()
                messages.success(request, "hod Added Successfully!")
                return HttpResponse("Successful")
        except:
                messages.error(request, "hod Added not Successfully!")
                return redirect('home')
             
            # return json.dumps({"code":1,"data":student.id})              
     
def simple_upload(request):
    if request.method == 'POST':
        Student_resource = StudentResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	# print(data[])
        	value = Student(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3]
        		)
        	value.save()       
        
    return render(request, 'input.html')