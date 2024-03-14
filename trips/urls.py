from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.view_trips, name='triplist'),
]