from django import forms



class userForm(forms.Form):
    email = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    college = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'College'}))
