from django.db import models
from django.db.models.signals import pre_save
from .jj_util import before_saving_article

# Create your models here.
class Meetup(models.Model):

  title = models.CharField(max_length=200)
  slug = models.SlugField(unique=True, blank=True)
  description = models.TextField()

pre_save.connect(before_saving_article, sender=Meetup)
