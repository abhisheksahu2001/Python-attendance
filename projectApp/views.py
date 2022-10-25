from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
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
        Name = request.POST.get("name")
        Enroll = request.POST.get("enroll")
        attend = request.POST.get("attend")
        date = request.POST.get("date")
        result= Student.objects.filter(Q(name=Name) & Q(enrollNo=Enroll) & Q(date_time=str(date)))
        if len(result) == 0:
            student1 = Student.objects.create(name=Name,enrollNo= Enroll, Attendance= attend, date_time =str(date))
            student1.save()
            print("created")
            return HttpResponse("success")
        else:
            result.update(Attendance= attend)
            print("updated")
            return HttpResponse("Updated")

        # if result is not None:
        #     result.update(Attendance=attend)
        #     print(result)
        # else:       
        #     # resultlist = list(result)
        #     # result.save()
        #     student1 = Student.objects.get_or_create(name=Name,enrollNo= Enroll, Attendance= attend, date_time =str(date))
        #     student1.save()
        #     print("created")
        #     return HttpResponse("none")

        # student1 = Student.objects.get_or_create(name=Name,enrollNo= Enroll, Attendance= attend, date_time =str(date))
        # student1.save()
        # if student1:
        #     new_student = Student.objects.create(id=str(id),name=Name,Attendance = attend,date_time=date)
        #     new_student.save()
        # Att_date = Student.objects.filter(date_time =date)
        # jsondata = json.loads(Att_date)
        # print(jsondata)
        # try:
        #     if id is not None:
        #         student = Student.objects.get(id=str(id))
        #         student.Attendance = attend
        #         student.date_time = date
        #         student.save()
        #         messages.success(request, "hod Added Successfully!")
        #         return HttpResponse("Successful")
        #     student1.save()
        # except:
        #         messages.error(request, "hod Added not Successfully!")
        #         return redirect('home')
        
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