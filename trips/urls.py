from django.urls import path
from . import views

urlpatterns = [
    path('trips/<int:pk>/', views.trip_detail, name='tripdetail'),
    path('trips/', views.view_trips, name='triplist'),
]