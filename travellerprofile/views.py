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

def view_profile(request):
    """
    Display an individual :model: travellerprofile.Traveller

    **Context**
    ``traveller``
        An instance of travellerprofile.Traveller

    **Template**
    :template: ``travellerprofile/view_traveller.html``
    """
    queryset = Traveller.objects.all()
    traveller = get_object_or_404(queryset, user=request.user)

    return render(
        request,
        "travellerprofile/view_profile.html",
        {
            "traveller": traveller,
        },
    )