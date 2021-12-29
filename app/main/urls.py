from django.urls import path

from . import views

# This file holds the URLs for the 'main' app
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("leaderboards/", views.leaderboards, name="leaderboards"),
    path("singleplayer/", views.singleplayer_menu, name="singleplayer_menu"),
    path("singleplayer/story/", views.singleplayer_story, name="singleplayer_story"),
]