from django.urls import path
from . import views

urlpatterns = [
  path("meetups/", views.index, name="meetups"),
  path('meetups/successful-registration/<slug:meetup_slug>/', views.registration_success, name="registration-success"),
  path('meetups/<slug:meetup_slug>/', views.meetup_details, name="meetup-details"),
]