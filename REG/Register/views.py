from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
from .models import Course,Student

def index(request):
    return render(request,"registers/index.html",{
        "Course": Course.objects.all()
    })


def ShowCourse(request, course_code):
    ShowCourse = get_object_or_404(Course,pk=course_code)
    return render(request,"registers/course_info.html",{
        "Course": ShowCourse,
    })

"""
def apply(request, course_code):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return HttpResponseRedirect(reverse("Users:login")+f"?next={request.path}")

    reg = get_object_or_404(Course, pk=course_code)
    if request.user not in Student.enrollment.all():
        reg.enrollment.add(request.user)
    return HttpResponseRedirect(reverse("Register:showcourse", args=(course_code,)))
"""
def apply(request , course_code):
    if request.method == "POST":
        select_subject = Course.objects.get(pk = course_code)
        student = Student.objects.get(pk = (request.user.id - 1))
        student.subject.add(select_subject)
    return HttpResponseRedirect(reverse("Register:ShowCourse"))