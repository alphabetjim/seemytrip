from django.shortcuts import render
from .models import Trip

# Create your views here.
def view_trips(request):
    """
    Display all trips that have been planned
    """
    queryset = Trip.objects.all()
    
    return render(
        request,
        'trips/triplist.html',
        {
            'queryset': queryset,
        }
    )