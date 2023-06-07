from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger, Airport
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
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all
    }
    return render(request, "flights/flight.html", context)


def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])           #获取在html文件中通过post提交的passenger变量数据， 对应<form action="{% url 'book' flight.id %}" method="post">
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No such flight"})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger"})
    
    passenger.flight.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

