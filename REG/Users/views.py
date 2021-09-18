from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from Register.models import Course
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    get_subject = request.user.enroll.all()
    return render(request, "users/studentinfo.html",{
        "subject":get_subject,
    })
        
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Users:studentinfo"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid Username or Password."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("Users:login"))
    