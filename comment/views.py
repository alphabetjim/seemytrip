from django.shortcuts import render
from django.views import generic
from .models import TripComment

# Create your views here.
class TripCommentList(generic.ListView):
    """
    Display all TripComments as a list
    """ 
    queryset = TripComment.objects.all()
    template_name = "comment/commentlist.html"
    paginate_by = 5