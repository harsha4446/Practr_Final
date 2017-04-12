from users.models import events, rounds
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
        fields = ['name', 'about', 'website', 'logo', 'inter_type' ]



class addRound(forms.ModelForm):
    title = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Round Title'}))
    sub_title = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Sub-Title (Optional)'}))
    task1 = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Task 1 (Required)'}))
    task2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Task 1 (Optional)'}))
    tast3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Task 1 (Optional)'}))
    task4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Task 1 (Optional)'}))
    task5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Task 1 (Optional)'}))
    resource1 = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Resource 1 (Required)'}))
    resource2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Resource 2(Optional)'}))
    resource3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Resource 3(Optional)'}))
    resource4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Resource 4(Optional)'}))
    resource5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Resource 5(Optional)'}))
    question1 = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Required'}))
    question2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}))
    question3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}))
    question4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}))
    question5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}))
    about = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'class': 'form-control','rows':9}))
    class Meta:
        model = rounds
        fields = ['title','sub_title', 'about','task1','task2','task4','tast3','task5','resource1'
                  ,'resource2','resource3','resource4','resource5','question1','question2','question3'
                  ,'question4','question5','creativity','content','communication','presentation','feasibility'
                  ,'rebuttal', 'feedback', 'ext_judge']