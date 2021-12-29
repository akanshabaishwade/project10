from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Picnic
from django.http import HttpResponse

# Create your views here.
def student_list(request):
    all_student_list = Picnic.objects.all()
    context = {
        'all_student_list' : all_student_list
    }

    return render(request, 'student_list.html', context)


def Add_student(request):
    if request.method == "POST":
        Name = request.POST['name']
        Class = request.POST['class']
        Fee = request.POST['fee']

        all_student_data = Picnic(student_name=Name, student_class=Class, student_fee=Fee)
        all_student_data.save()
        return HttpResponse("Student Sucessfully added...")

    return render(request, 'add_student.html')


def delete(request, id):
    if request.method == "POST":
        all_data = Picnic.objects.get(pk=id)
        all_data.delete()
        return redirect('/')

