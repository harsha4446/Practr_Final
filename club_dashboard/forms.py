from users.models import events
from django import forms

class openRegistarion(forms.ModelForm):
    registration = forms.BooleanField()
    class Meta:
        model = events
        fields = ['registration',]


class addEvent(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 30}))
    website = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = events
        fields = ['name', 'about', 'website', ]