from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView, name="home"),
    path("about", views.AboutPageView, name="about"),
]
