from users.models import events, rounds, round_scores, round_room, room_judge
from django import forms
from django.forms.extras import SelectDateWidget


class addEvent(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 30}))
    website = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(required=False)
    team_size1 = forms.IntegerField(required=False)
    team_size2 = forms.IntegerField(required=False)
    team_size3 = forms.IntegerField(required=False)
    team_size4 = forms.IntegerField(required=False)
    team_size5 = forms.IntegerField(required=False)
    team_size6 = forms.IntegerField(required=False)
    class Meta:
        model = events
        fields = ['name', 'about', 'website', 'logo', 'inter_type', 'marketing',
                  'finance', 'public_relations', 'human_resources', 'ent_dev', 'best_manager',
                  'team_size1', 'team_size2', 'team_size3', 'team_size4', 'team_size5', 'team_size6']


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


class scoreForm(forms.ModelForm):
    question1 = forms.CharField(label="", required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    question2 = forms.CharField(label="", required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    question3 = forms.CharField(label="", required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    question4 = forms.CharField(label="", required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    question5 = forms.CharField(label="", required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    feedback = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9}))
    communication = forms.IntegerField(label="", required=False)
    content = forms.IntegerField(label="", required=False)
    creativity = forms.IntegerField(label="", required=False)
    rebuttal = forms.IntegerField(label="", required=False)
    feasibility = forms.IntegerField(label="", required=False)
    class Meta:
        model = round_scores
        fields = ['question1','question2','question3','question4','question5','communication','content',
                  'creativity','feedback','rebuttal','feasibility',]


class toggles(forms.Form):
    live = forms.BooleanField(forms.CheckboxInput(attrs={'class':'togglebutton'}))
    active = forms.BooleanField(forms.CheckboxInput(attrs={'class':'togglebutton'}))


class rooms(forms.ModelForm):

    class Meta:
        model = round_room
        fields = ['room',]


class deadlines(forms.Form):
    deadline = forms.DateField()

class newJudge(forms.ModelForm):
    judge_email = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Judge Email'}))
    judge_password = forms.CharField(label="", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    class Meta:
        model = room_judge
        fields = ['judge_email', 'judge_password']