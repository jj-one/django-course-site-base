from django import forms
from .models import Participant

class RegistrationForm(forms.Form):

  email = forms.EmailField(max_length=200, required=True, label="Enter your email:")
    