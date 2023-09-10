from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.
def index(request):
  meetups = Meetup.objects.all()
  context = {"meetups": meetups}
  return render(request, "meetups/index.html", context)

def meetup_details(request, meetup_slug):
  registration_form = RegistrationForm()
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
  except Exception as _:
    return render(request, "meetups/meetup-details.html", {"found": False, "form": registration_form})
  if request.method == "POST":
    registration_form = RegistrationForm(request.POST)
    if registration_form.is_valid():
      email = registration_form.cleaned_data["email"]
      participant, _ = Participant.objects.get_or_create(email=email)
      # participant = registration_form.save()
      selected_meetup.participant.add(participant)
      return redirect("registration-success", selected_meetup.slug)
  
  context = {"found": True, "selected_meetup": selected_meetup, "form": registration_form}
  return render(request, "meetups/meetup-details.html", context)

def registration_success(request, meetup_slug):
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
  except Exception as _:
    return render(request, "meetups/index.html", {})
  
  context = {"selected_meetup": selected_meetup}
  return render(request, 'meetups/registration-success.html', context)