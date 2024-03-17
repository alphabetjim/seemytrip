from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Trip
from .forms import TripForm
from comment.models import TripComment
from comment.forms import TripCommentForm
from travellerprofile.models import Traveller

# Create your views here.
def view_trips(request):
    """
    Display all trips that have been planned
    """
    queryset = Trip.objects.all()
    # template reuse
    traveller_own = False

    return render(
        request,
        'trips/triplist.html',
        {
            'queryset': queryset,
            'traveller_own': traveller_own,
        }
    )

def view_own_trips(request):
    """
    Display only trips planned by current traveller
    """

    # Ensure that page cannot be accessed just by entering URL
    if request.user.is_authenticated:
        try:
            traveller = get_object_or_404(Traveller, user=request.user)
        except:
            return HttpResponseRedirect(reverse('home'))
        else:
            queryset = Trip.objects.all().filter(planner = traveller)
    
    # reuse the triplist template
    traveller_own = True

    return render(
        request,
        'trips/triplist.html',
        {
            'queryset': queryset,
            'traveller_own': traveller_own,
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

def comment_edit(request, trip_pk, tc_pk):
    """
    Display an individual TripComment for edit.

    **Context**

    ``trip``
        An instance of :model:`trips.Trip`.
    ``tripcomment``
        A single comment related to the trip.
    ``tripcomment_form``
        An instance of :form:`comment.TripCommentForm`
    """
    if request.method == "POST":

        trip = get_object_or_404(Trip, pk=trip_pk)
        tripcomment = get_object_or_404(TripComment, pk=tc_pk)
        tripcomment_form = TripCommentForm(data=request.POST, instance=tripcomment)

        if tripcomment_form.is_valid() and tripcomment.author == request.user:
            tripcomment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('tripdetail', args=[trip_pk]))

def comment_delete(request, pk, comment_id):
    """
    Delete an individual trip comment.

    **Context**

    ``trip``
        An instance of :model:`trips.Trip`.
    ``tripcomment``
        A single comment related to the trip.
    """
    trip = get_object_or_404(Trip, pk=pk)
    tripcomment = get_object_or_404(TripComment, pk=comment_id)

    if tripcomment.author == request.user:
        tripcomment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
            'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('tripdetail', args=[pk]))

def create_trip(request):
    """
    Display form to allow traveller creation of a .models:Trip instance
    """
    traveller = get_object_or_404(Traveller, user = request.user)
    if request.method == "POST":
        trip_form = TripForm(request.POST, request.FILES)
        if trip_form.is_valid():
            trip = trip_form.save(commit=False)
            trip.planner = traveller
            trip.save()
            return HttpResponseRedirect(reverse('owntriplist'))
    else:
        trip_form = TripForm()
    edit = False
    return render(
        request,
        "trips/create_trip.html",
        {
            'trip_form': trip_form,
            'edit': edit,
        },)

def edit_trip(request, pk):
    """
    Display form to allow a traveller to edit their trip
    """
    trip = get_object_or_404(Trip, pk=pk)
    if trip.planner.user.username == request.user.username:
        print('User authentication passed')
        if request.method == "POST":
            trip_form = TripForm(request.POST, request.FILES, instance = trip)
            if trip_form.is_valid():
                trip_form.save()
                messages.add_message(request, messages.SUCCESS, 'Trip Updated!')
                return HttpResponseRedirect(reverse('tripdetail', args=[pk]))
            else:
                messages.add_message(request, messages.ERROR,
                    'Error updating trip.')
        else:
            trip_form = TripForm(instance = trip)
        edit = True
        return render(
            request,
            "trips/create_trip.html",
            {
                "trip_form": trip_form,
                "edit": edit,
                "trip": trip,
            },
        )
    else:
        return HttpResponseRedirect(reverse('triplist'))

def delete_trip(request, pk):
    """
    View to allow trip deletion
    """
    trip = get_object_or_404(Trip, pk=pk)
    if trip.planner.user.username == request.user.username:
        trip.delete()
        messages.add_message(request, messages.SUCCESS, 'Trip deleted!')
    else:
        # Shouldn't be possible for a non-planner user or traveller to be
        # on this page, but:
        messages.add_message(request, messages.ERROR,
            'You can only delete your own trips!')

    return HttpResponseRedirect(reverse('owntriplist'))
    