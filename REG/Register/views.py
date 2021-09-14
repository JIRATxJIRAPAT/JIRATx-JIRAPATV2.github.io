from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
from .models import Course

def index(request):
    return render(request,"registers/index.html",{
        "Course": Course.objects.all()
    })


def ShowCourse(request, course_code):
    output = get_object_or_404(Course,pk=course_code)
    return render(request,"registers/course_info.html",{
        "Course": output,
        "member": output.enrollment.all()
    })


def apply(request, course_code):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return HttpResponseRedirect(reverse("Users:login")+f"?next={request.path}")

    showcourse = get_object_or_404(Course, pk=course_code)
    if request.user not in showcourse.enrollment.all():
        showcourse.enrollment.add(request.user)
    return HttpResponseRedirect(reverse("Register:apply", args=(course_code,)))