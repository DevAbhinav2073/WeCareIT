from django.contrib import admin
from django.urls import path

from apps.main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-journey/', JourneyCreateCreateView.as_view(), name='create_journey'),
    path('list-passenger/', passenger_list_page, name='list_passenger'),
    path('list-vehicle/', vehicle_list_page, name='list_vehicle'),
]
