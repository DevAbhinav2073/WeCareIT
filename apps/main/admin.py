from django.contrib import admin

# Register your models here.
from apps.main.models import Journey, Vehicle

admin.site.register(Vehicle)
admin.site.register(Journey)
