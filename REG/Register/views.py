from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Course,Student

def index(request):
    return render(request,"registers/index.html",{
        "Course": Course.objects.all()
    })


def ShowCourse(request, course_code):
    output = get_object_or_404(Course,pk=course_code)
    return render(request,"registers/course_info.html",{
        "Course": output,
        "member": Student.member.all()
    })
