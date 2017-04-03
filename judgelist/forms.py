from django import forms

class userForm(forms.Form):
    email = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    interest = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Field'}))
    name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))

