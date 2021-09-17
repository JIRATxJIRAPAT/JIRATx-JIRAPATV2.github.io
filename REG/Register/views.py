from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Course
# Create your views here.


def index(request):
    return render(request,"registers/index.html",{
        "Course": Course.objects.all()
    })


def ShowCourse(request, course_code):
    info = get_object_or_404(Course,pk=course_code)
    return render(request,"registers/course_info.html",{
        "Course": info,
        "student":info.student.all(),
        #"non_enrollment": Student.objects.exclude(enrollment=info),
    })


def apply(request, course_code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course,pk=course_code)
    if request.user not in x.student.all():
        x.student.add(request.user)
    return HttpResponseRedirect(reverse("Register:ShowCourse",args=(course_code,)))
        

"""
def apply(request, course_code):
    
    if request.method == "POST":
        x = get_object_or_404(Course,pk=course_code)
        student = request.POST["student"]
        x.enroll.add(student)
        return HttpResponseRedirect(reverse("Register:ShowCourse", args=(course_code,))
        )
"""

"""
def unapply(request , course_code):
    if request.method == "POST":
        select_course = get_object_or_404(Course,pk=course_code)
        student = request.POST["students"]
        select_course.enroll.remove(student)
    return HttpResponseRedirect(reverse("Register:index"))
"""