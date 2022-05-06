from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView
from django.template.response import TemplateResponse
from django.contrib.auth import get_user_model

from apps.main.models import Journey, Vehicle

User = get_user_model()


class JourneyCreateCreateView(CreateView):
    model = Journey
    fields = [
        'vehicle',
        'driver',
        'passengers',
        'distance_travelled'
    ]


def vehicle_list_page(request):
    vehicles = Vehicle.objects.all()
    data = {
        'vehicles': vehicles
    }
    return TemplateResponse(request, 'main/vehicle_detail.html', context=data)


def passenger_list_page(request):
    passengers = User.objects.all()
    data = {
        'passengers': passengers
    }
    return TemplateResponse(request, 'main/passenger_detail.html', context=data)


def home(request):
    return TemplateResponse(request, 'main/home.html')
