from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Traveller
from .forms import TravellerForm


# Create your views here.
def homepage(request):
    """
    View to display home page
    """

    return render(
        request,
        'travellerprofile/index.html',
        {},
    )

class TravellerList(generic.ListView):
    """
    Returns all Traveller profiles in :model:`travellerprofile:Traveller`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`travellerprofile:Traveller`

    **Template:**

    :template:`travellerprofile/index.html`
    """
    queryset = Traveller.objects.all()
    print(queryset.first())
    template_name = "travellerprofile/travellerlist.html"