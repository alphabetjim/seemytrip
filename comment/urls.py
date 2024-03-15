from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripCommentList, name='tripcommentlist'),
    path('edit_tripcomment/<int:pk>', views.comment_edit, name='edit_tripcomment'),
]