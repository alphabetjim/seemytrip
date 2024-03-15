from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripCommentList, name='tripcommentlist'),
]