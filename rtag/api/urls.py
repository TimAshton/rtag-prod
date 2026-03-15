from django.urls import path
from . import views

urlpatterns = [
    path("challenge/<id>", views.ChallengeAPIView.as_view()),
    path("challenges", views.ChallengesAPIView.as_view()),
]
