from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Course,Student
# Create your views here.


def index(request):
    return render(request,"registers/index.html",{
        "Course": Course.objects.all()
    })


def ShowCourse(request, course_code):
    x = get_object_or_404(Course,pk=course_code)
    return render(request,"registers/course_info.html",{
        "Course": x,
        "student":x.enroll.all(),
        "non_enrollment": Student.objects.exclude(enrollment=x)
    })


def apply(request, course_code):
    if request.method == "POST":
        x = Course.objects.filter(Course,pk=course_code)
        student = request.POST["student"]
        x.enroll.add(student)
        return HttpResponseRedirect(reverse("Register:ShowCourse", args=(course_code,))
        )