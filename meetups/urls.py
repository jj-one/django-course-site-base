from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="meetups"),
  path('successful-registration/<slug:meetup_slug>/', views.registration_success, name="registration-success"),
  path('<slug:meetup_slug>/', views.meetup_details, name="meetup-details"),
]