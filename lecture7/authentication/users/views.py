from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
            "user": request.user
    } 
    return render(request, "users/user.html, context")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))  #Redirect重定向到index函数， reverse的作用是通过函数名反查url，和urls.py中函数名与url路径关联有关
    else:
        return render(request, "users/login.html"), {"message": "Invalid credit"}
    

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})