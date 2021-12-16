from django.urls import path

from . import views

# This file holds the URLs for the 'main' app
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("leaderboards/", views.leaderboards, name="leaderboards"),
]