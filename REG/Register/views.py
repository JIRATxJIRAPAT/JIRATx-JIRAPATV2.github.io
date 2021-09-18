from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Course
from django.db.models import Count

# Create your views here.


def index(request):
    
    return render(request,"registers/index.html",{
        "Course": Course.objects.all(),
        
    })


def ShowCourse(request, course_code):
    info = get_object_or_404(Course,pk=course_code)
    students = info.student.all()

    return render(request,"registers/course_info.html",{
        "Course": info,
        "student":info.student.all(),
        "seat":students.count()
    })


def apply(request, course_code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course,pk=course_code)
    if request.user not in x.student.all():
        x.student.add(request.user)
        x.siting += 1 
    return HttpResponseRedirect(reverse("Register:ShowCourse",args=(course_code,)))


def removeCourse(request , course_code):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course,pk=course_code)
    if request.user in x.student.all():
        x.student.remove(request.user)
        x.siting -=  1
    return HttpResponseRedirect(reverse("Register:ShowCourse",args=(course_code,)))
    
   