from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('/rooms', views.rooms_details, name='Rooms'),
    path('/new', views.new, name='newMeeting')
]