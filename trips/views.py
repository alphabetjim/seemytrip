from django.shortcuts import render, get_object_or_404, reverse
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

def trip_detail(request, pk):
    """
    Display detailed view of a trip
    """
    queryset = Trip.objects.all()
    trip = get_object_or_404(queryset, pk=pk)
    
    return render(
        request,
        'trips/trip_detail.html',
        {
            'trip': trip,
        }
    )