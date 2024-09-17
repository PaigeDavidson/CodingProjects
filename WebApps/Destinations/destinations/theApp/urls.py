from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/new/", views.new_user, name="new_user"),
    path("sessions/new/", views.new_session, name="new_session"),
    path("destinations/", views.destinations, name="destinations"),
    path("destinations/new/", views.new_destination, name="new_destination"),
    path("destinations/<int:id>/", views.destination, name="destination"),
    path("POST/destinations/<int:id>/", views.POSTdestination, name = "POSTdestination"),
    path("destinations/<int:id>/destroy", views.destroyDestination, name = "destroyDestination"),
    path("sessions/destroy/", views.destroySession, name = "destroySession")
]