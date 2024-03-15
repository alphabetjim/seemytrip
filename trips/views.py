from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trip
from comment.forms import TripCommentForm

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
    tripcomments = trip.tripcomments.all().order_by("-created_on")
    tripcomment_count = trip.tripcomments.count()
    
    if trip.followers.filter(username=request.user.username).exists():
        user_following = True
    else:
        user_following = False
    
    # Allow users to add a comment
    if request.method == "POST":
        tripcomment_form = TripCommentForm(data=request.POST)
        if tripcomment_form.is_valid():
            tripcomment = tripcomment_form.save(commit=False)
            tripcomment.author = request.user
            tripcomment.trip = trip
            tripcomment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Trip Comment submitted.'
            )

    tripcomment_form = TripCommentForm()

    return render(
        request,
        'trips/trip_detail.html',
        {
            'tripcomments': tripcomments,
            'tripcomment_count': tripcomment_count,
            'trip': trip,
            'user_following': user_following,
            'tripcomment_form': tripcomment_form,
        }
    )

def follow_trip(request, pk):
    """
    Toggle whether or not a user is following a trip
    """
    trip = get_object_or_404(Trip, pk=pk)

    if trip.followers.filter(username=request.user.username).exists():
        trip.followers.remove(request.user)
        messages.add_message(request, messages.SUCCESS, 'You are no longer following this trip!')
    else:
        trip.followers.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'You are now following this trip!')

    return(HttpResponseRedirect(f'../../trips/{pk}'))