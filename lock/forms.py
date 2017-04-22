from django import forms


class inform(forms.Form):
    password = forms.CharField(label="",required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))