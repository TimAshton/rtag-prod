from django.urls import path
from . import views

urlpatterns = [
    path("challenge/<id>", views.challenge),
    path("challenges", views.challenges),
]
