from django.db import models
from django.db.models import Sum, Q
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    It's always a better approach to extend the abstract user class and create your own User model
    """
    @property
    def total_distance_travelled(self):
        return Journey.objects.filter(Q(driver=self) | Q(passengers=self)).distinct().aggregate(
            total_distance_travelled=Sum('distance_travelled')).get(
            'total_distance_travelled') or 0


class Vehicle(models.Model):
    """
    This model will store the vehicle information. For now only minimal fields are added
    """
    registration_number = models.CharField(max_length=50, unique=True)
    make_year = models.IntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    @property
    def total_distance_travelled(self):
        return self.journeys.all().aggregate(total_distance_travelled=Sum('distance_travelled')).get(
            'total_distance_travelled') or 0

    def __str__(self):
        return self.registration_number


class Journey(models.Model):
    """
    This model will store the journey details of all the journeys taken by every vehicle

    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='journeys')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    passengers = models.ManyToManyField(User, blank=True)
    distance_travelled = models.DecimalField(decimal_places=1, max_digits=10)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('list_vehicle')

    @property
    def total_passengers_count(self):
        return self.passengers.all().count() + 1  # +1 is for driver

    def __str__(self):
        return f'{self.vehicle} travelled {self.distance_travelled} with {self.total_passengers_count} passenger(s)'
