from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripCommentList.as_view(), name='tripcommentlist'),
]