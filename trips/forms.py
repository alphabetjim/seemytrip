from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    """
    Form class for travellers to create a Trip
    """
    itinerary = forms.CharField(widget=forms.Textarea(attrs={'type': 'text','rows': 4, 'cols': 40}))
    trip_photo = forms.ImageField()
    startDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    endDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Trip
        fields = ('name', 'region', 'accomm_type', 'itinerary', 
            'interests', 'startDate', 'endDate', 'trip_photo',)