from django.shortcuts import render
from django.views import generic
from .models import TripComment

# Create your views here.
def TripCommentList(request):
    """
    Display all TripComments as a list
    """ 
    queryset = TripComment.objects.all()
    template_name = "comment/commentlist.html"
    
    return render(
        request,
        template_name,
        {
            'queryset': queryset,
        }
    )

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
            tripcomment = tripcomment_form.save(commit=False)
            tripcomment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('tripdetail', args=[trip_pk]))

# def comment_delete(request, comment_id):
#     """
#     Delete an individual trip comment.

#     **Context**

#     ``trip``
#         An instance of :model:`trips.Trip`.
#     ``tripcomment``
#         A single comment related to the trip.
#     """
#     trip = get_object_or_404(Trip, pk=trip_pk)
#     tripcomment = get_object_or_404(TripComment, pk=comment_id)

#     if tripcomment.author == request.user:
#         tripcomment.delete()
#         messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
#     else:
#         messages.add_message(request, messages.ERROR,
#             'You can only delete your own comments!')

#     return HttpResponseRedirect(reverse('tripdetail', args=[trip_pk]))
