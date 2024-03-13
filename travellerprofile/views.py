from django.shortcuts import render

# Create your views here.
def testview(request):
    """
    Simple view to display a template
    """

    return render(
        request,
        'travellerprofile/index.html',
        {},
    )