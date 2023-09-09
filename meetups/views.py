from django.shortcuts import render
from .models import Meetup

# Create your views here.
def index(request):
  meetups = Meetup.objects.all()
  context = {"meetups": meetups}
  return render(request, "meetups/index.html", context)

def meetup_details(request, meetup_slug):
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
  except Exception as _:
    return render(request, "meetups/meetup-details.html", {"found": False})
  
  context = {"found": True, "selected_meetup": selected_meetup}
  return render(request, "meetups/meetup-details.html", context)