from django.shortcuts import render
from .models import Trip

# Create your views here.
def view_trips(request):
    """
    Display all trips that have been planned
    """
    queryset = Trip.objects.all()
    accomm_types = []
    for trip in queryset:
        if trip.accomm_type is not None:
            accomm_types.append(Trip.ACCOMM_OPTIONS[trip.accomm_type][1])
        else:
            accomm_types.append("")
    print(accomm_types)
    return render(
        request,
        'trips/triplist.html',
        {
            'queryset': queryset,
            'accomm_types': accomm_types,
        }
    )