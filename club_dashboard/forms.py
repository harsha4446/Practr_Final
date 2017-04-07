from users.models import events
from django import forms

class openRegistarion(forms.ModelForm):
    registration = forms.BooleanField()
    class Meta:
        model = events
        fields = ['registration',]