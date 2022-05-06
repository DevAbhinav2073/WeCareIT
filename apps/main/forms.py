from django import forms

from apps.main.models import Journey


class JourneyCreateForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = [
            'vehicle',
            'driver',
            'passengers',
            'distance_travelled'
        ]
