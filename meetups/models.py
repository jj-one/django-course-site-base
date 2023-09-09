from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .jj_util import before_saving_article

# Create your models here.
class Location(models.Model):

  name = models.CharField(max_length=200)
  address = models.CharField(max_length=240)

  def __str__(self):
    return f"{self.name} -> ({self.address})"

class Participant(models.Model):

  email = models.EmailField(unique=True)

  def __str__(self):
    return self.email

class Meetup(models.Model):

  title = models.CharField(max_length=200)
  organizer = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
  date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
  slug = models.SlugField(unique=True, blank=True)
  description = models.TextField()
  image = models.ImageField(upload_to="images")
  location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
  participant = models.ManyToManyField(Participant, blank=True)

  def __str__(self):
    return f"{self.title} -> ({self.slug})"


pre_save.connect(before_saving_article, sender=Meetup)
