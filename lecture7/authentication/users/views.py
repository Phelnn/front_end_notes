from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:                               #user是request对象里包含的一个属性（其本身也是对象），可以通过login()、logout()等函数改变状态
        return render(request, "users/login.html", {"message": None})
    context = {
            "user": request.user
    } 
    return render(request, "users/user.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)  #看起来是个能读取用户库的函数，验证用户名和密码是否正确，正确的话返回详细的用户信息，否则返回none
    if user is not None:
        login(request, user)
        #疑问：为什么不直接调用index函数而是使用下面的方式？因为下面的方式会重新发起http请求并进行连接，直接调用index(request)不会收到回传的HttpResposeObject，浏览器会报错
        return HttpResponseRedirect(reverse("index"))  #Redirect重定向到index函数， reverse的作用是通过函数名反查url，和urls.py中函数名与url路径关联有关
    else:
        return render(request, "users/login.html", {"message": "Invalid credit"})
    

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})