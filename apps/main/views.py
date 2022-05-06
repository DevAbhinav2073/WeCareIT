from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView
from django.template.response import TemplateResponse
from django.contrib.auth import get_user_model

from apps.main.models import Journey, Vehicle

User = get_user_model()


class JourneyCreateCreateView(CreateView):
    """
    This view will handle the journey creation. After the journey is created, the user is redirected to the
    vehicle list page where the information about the vehicles are displayed
    """
    model = Journey
    fields = [
        'vehicle',
        'driver',
        'passengers',
        'distance_travelled'
    ]


def vehicle_list_page(request):
    """
    This view will display the list of vehicles with the total distance travelled information
    """
    vehicles = Vehicle.objects.all()
    data = {
        'vehicles': vehicles
    }
    return TemplateResponse(request, 'main/vehicle_detail.html', context=data)


def passenger_list_page(request):
    """
        This view will display the list of passengers with the total distance travelled information

    """

    passengers = User.objects.all()
    data = {
        'passengers': passengers
    }
    return TemplateResponse(request, 'main/passenger_detail.html', context=data)


def home(request):
    """
    This is simply the homepage that contains the link to different 3 pages
    """
    return TemplateResponse(request, 'main/home.html')
