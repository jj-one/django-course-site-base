from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Meetup, Location, Participant

class MeetupAdmin(admin.ModelAdmin):
  pass
  list_display = ("title", "location", "date")
  list_filter = ("location","date")


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
