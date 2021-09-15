from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from Register.models import Student
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    
    return render(request, "Users/studentinfo.html")
        
    



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Users:studentinfo"))
        else:
            return render(request, "Users/login.html",{
                "message": "Invalid Credential."
            })

    return render(request, "Users/login.html")

def logout_view(request):
    logout(request)

    return render(request, "Users/login.html",{
        "message": "Logged out."
    })