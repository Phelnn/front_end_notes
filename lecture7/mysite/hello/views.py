from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Flight
# Create your views here.


def index(request):    #比flask多了个request的参数，少了@app('/')
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight
    }
    return render(request, "flights/flight.html", context)