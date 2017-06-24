from django import forms
from . models import student, interests, student_detail,judge_detail,colleges,clubs
from django.contrib.auth import (authenticate,login,logout,get_user_model)


User = get_user_model()

class RegisterModel(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    phoneno = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone','min':'10','max':'10'}))
    class Meta:
        model = student
        fields = ['email','password','name','phoneno',]


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', }))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(email=username, password=password)
        if user is None:
            raise forms.ValidationError("Incorrent Username or Password")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrent Password")
        return super(LoginForm, self).clean()



class defaultForm(forms.ModelForm):
    about = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':4}))
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = student
        fields = ['profile_picture', 'location', 'about', ]


class StudentInfo(forms.ModelForm):
    class Meta:
        model = student_detail
        fields = ['degree', 'year', 'section']



class JudgeInfo(forms.ModelForm):
    degree = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    college = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = judge_detail
        fields = ['degree', 'designation', 'industry_exp', 'website', 'college']


class interestModel(forms.ModelForm):
    class Meta:
        model = interests
        fields = ['marketing', 'finance', 'public_relations', 'human_resources', 'ent_dev', 'best_manager']


class newCollege(forms.ModelForm):
    address = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(required=False)
    class Meta:
        model = colleges
        fields = ['college_name','address','logo']

class newClub(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    admin_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    club_password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    club_email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = clubs
        fields = ['name','admin_name','club_password','club_email', 'phone']

class clubsetup(forms.ModelForm):
    video = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':4}))
    logo = forms.ImageField(required=False)
    class Meta:
        model = clubs
        fields = ['video','website','about', 'logo']