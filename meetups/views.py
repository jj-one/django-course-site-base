from django.shortcuts import render

# Create your views here.
def index(request):
  meetups = [
    {
      "title": "Main Meetup for All", 
      "slug": "hagd-rfd-vad",
      "location": "Sacred Heart College Apapa", 
      "address": "12 - 16 Child Avenue, Apapa, Lagos",
      "description": "Nulla a purus sed mi faucibus maximus. Donec vestibulum lobortis tortor, a malesuada lacus feugiat non.",
    },
    {
      "title": "Home Coming", 
      "slug": "gbcf-fae",
      "location": "Akpugo Eze", 
      "address": "Iga Village, Obinagu Uwani Akpugo",
      "description": "Morbi tortor quam, fringilla in orci eget, facilisis efficitur augue.",
    },
    {
      "title": "Just for Dev", 
      "slug": "vhfa-jf",
      "location": "VS Code", 
      "address": "VS Code Live Share via GitHub your account",
      "description": "Cras vestibulum enim ullamcorper dolor maximus pulvinar.",
    },
  ]
  context = {"meetups": meetups}
  return render(request, "meetups/index.html", context)

def meetup_details(request, meetup_slug):
  selected_meetup = {
      "title": "Home Coming", 
      "slug": "gbcf-fae",
      "location": "Akpugo Eze", 
      "address": "Iga Village, Obinagu Uwani Akpugo",
      "description": "Morbi tortor quam, fringilla in orci eget, facilisis efficitur augue.",
    }

  context = {"selected_meetup": selected_meetup}
  return render(request, "meetups/meetup-details.html", context)