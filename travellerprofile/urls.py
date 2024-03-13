from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('travellers/', views.TravellerList.as_view(), name='travellerlist'),
    path('travellerprofile/view_profile/', views.view_profile, name='view_traveller'),
]