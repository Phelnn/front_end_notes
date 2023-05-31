from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):    #比flask多了个request的参数，少了@app('/')
    return HttpResponse("Hello, world!")

