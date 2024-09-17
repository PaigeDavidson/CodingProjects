from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="indexPage"),
    path("activity/<int:id>/", views.activity, name="activity"),
    path("new_activity/", views.new_activity, name="new_activity"),
    path("activity/<int:id>/new_timelog/", views.new_timelog, name="new_timelog")
]