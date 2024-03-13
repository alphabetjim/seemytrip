from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
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

def TravellerList(request):
    """
    Returns all Traveller profiles in :model:`travellerprofile:Traveller`
    and displays them in a page.
    **Context**

    ``queryset``
        All published instances of :model:`travellerprofile:Traveller`

    **Template:**

    :template:`travellerprofile/index.html`
    """
    queryset = Traveller.objects.all()
    template_name = "travellerprofile/travellerlist.html"
    return render(
        request,
        template_name,
        {
            'queryset': queryset,
        },
    )

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

def create_traveller(request):
    """
    Display form to allow user creation of a .models:Traveller instance
    """
    context = {}
    if request.method == "POST":
        form = TravellerForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            bio = form.cleaned_data.get("bio")
            img = form.cleaned_data.get("profile_photo")
            obj = Traveller.objects.create(
                                 user = request.user,
                                 firstname = firstname, 
                                 lastname = lastname, 
                                 bio = bio, 
                                 profile_photo = img
                                 )
            obj.save()
            return HttpResponseRedirect(reverse(view_profile))
    else:
        form = TravellerForm()
    context['form'] = form
    return render(
        request,
        "travellerprofile/create_traveller.html",
        context,)