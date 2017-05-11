from django import forms
from . models import student, interests, student_detail,judge_detail,colleges,clubs
from django.contrib.auth import (authenticate,login,logout,get_user_model)
from django.forms.extras import SelectDateWidget

user = get_user_model()

class RegisterModel(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    phoneno = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    class Meta:
        model = student
        fields = ['email','password','name','phoneno',]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', }))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control'}))


DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018',)


class defaultForm(forms.ModelForm):
    dob = forms.DateField(widget=SelectDateWidget(years=DOY, attrs={'class': 'form-control'}))
    location = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':6}))
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = student
        fields = ['profile_picture', 'location', 'dob', 'about', ]


class StudentInfo(forms.ModelForm):
    degree = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = student_detail
        fields = ['degree', 'year',]



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
        fields = ['marketing', 'finance', 'public_relations', 'human_resources', 'ent_dev', 'business_quiz']


class newCollege(forms.ModelForm):
    college_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = colleges
        fields = ['college_name','address','phone']

class newClub(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    admin_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    club_password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    club_email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo = forms.ImageField(required=False)
    class Meta:
        model = clubs
        fields = ['name','admin_name','club_password','club_email', 'phone', 'logo']

class clubsetup(forms.ModelForm):
    video = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = clubs
        fields = ['video','website','about']