from users.models import events, rounds, round_scores, round_room, room_judge
from django import forms
from django.forms.extras import SelectDateWidget


class addEvent(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'id':'name','class': 'form-control','value':'Trying'}))
    about = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'id':'about2','class': 'form-control', 'rows': 3}))
    website = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'website','class': 'form-control'}))
    logo = forms.ImageField(required=False)
    class Meta:
        model = events
        fields = ['name', 'about', 'website', 'logo', 'inter_type', 'marketing',
                  'finance', 'public_relations', 'human_resources', 'ent_dev', 'best_manager',
                  'corp_strg','quiz','team',]


class addRound(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'title','class': 'form-control'}))
    sub_title = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'subtitle','class': 'form-control'}))
    task1 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'task1','style':'display:block','class': 'form-control','placeholder':'Task 1 (Required)'}))
    task2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'task2','style':'display:none','class': 'form-control','placeholder':'Task 2 (Optional)'}))
    task3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'task3','style':'display:none','class': 'form-control','placeholder':'Task 3 (Optional)'}))
    task4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'task4','style':'display:none','class': 'form-control','placeholder':'Task 4 (Optional)'}))
    task5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'task5','style':'display:none','class': 'form-control','placeholder':'Task 5 (Optional)'}))
    resource1 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'resource1','style':'display:block','class': 'form-control','placeholder': 'Resource 1 (Required)'}))
    resource2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'resource2','style':'display:none','class': 'form-control','placeholder':'Resource 2(Optional)'}))
    resource3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'resource3','style':'display:none','class': 'form-control','placeholder':'Resource 3(Optional)'}))
    resource4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'resource4','style':'display:none','class': 'form-control','placeholder':'Resource 4(Optional)'}))
    resource5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'resource5','style':'display:none','class': 'form-control','placeholder':'Resource 5(Optional)'}))
    question1 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'question1','class': 'form-control','placeholder':'Custom 1 (Optional)'}))
    question2 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'question2','class': 'form-control','placeholder':'Custom 2(Optional)'}))
    question3 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'question3','class': 'form-control','placeholder':'Custom 3(Optional)'}))
    question4 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'question4','class': 'form-control','placeholder':'Custom 4(Optional)'}))
    question5 = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'id':'question5','class': 'form-control','placeholder':'Custom 5(Optional)'}))
    about = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'id':'mce','class': 'form-control','rows':9,'maxlength':30000}))
    creativity=forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id':'creativity'}))
    presentation = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id': 'presentation'}))
    content = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id': 'content'}))
    rebuttal = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id': 'rebuttal'}))
    communication = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id': 'communication'}))
    feasibility = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id': 'feasibility'}))
    core1 = forms.IntegerField(label="", required=False, widget=forms.NumberInput(attrs={'id':'core1','style':'width:100px','class': 'form-control', 'value':'0','onchange':'fetch()'}))
    core2 = forms.IntegerField(label="", required=False, widget=forms.NumberInput(
        attrs={'id': 'core2', 'style': 'width:100px', 'class': 'form-control', 'value':'0','onchange':'fetch()'}))
    core3 = forms.IntegerField(label="", required=False, widget=forms.NumberInput(
        attrs={'id': 'core3', 'style': 'width:100px', 'class': 'form-control', 'value':'0','onchange':'fetch()'}))
    core4 = forms.IntegerField(label="", required=False, widget=forms.NumberInput(
        attrs={'id': 'core4', 'style': 'width:100px', 'class': 'form-control', 'value':'0','onchange':'fetch()'}))
    core5 = forms.IntegerField(label="", required=False, widget=forms.NumberInput(
        attrs={'id': 'core5', 'style': 'width:100px', 'class': 'form-control', 'value':'0','onchange':'fetch()'}))
    class Meta:
        model = rounds
        fields = ['title','sub_title', 'about','task1','task2','task4','tast3','task5','resource1'
                  ,'resource2','resource3','resource4','resource5','question1','question2','question3'
                  ,'question4','question5','creativity','content','communication','presentation','feasibility'
                  ,'rebuttal', 'feedback', 'core1','core2','core3','core4','core5',]


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