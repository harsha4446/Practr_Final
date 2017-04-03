from django.shortcuts import render
from . models import student, interests, student_detail
from .forms import RegisterModel,LoginForm, StudentInfo, JudgeInfo, interestModel, defaultForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .models import student as User


# Create your views here.

def index(request):
    form = RegisterModel(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['email']
        password=form.cleaned_data['password']
        name = form.cleaned_data['name']
        phoneno = form.cleaned_data['phoneno']
        new_user=User.objects.create_user(username,password,name,phoneno)
        new_user.save()
    formin = LoginForm(request.POST or None)
    if formin.is_valid():
        username = formin.cleaned_data.get("username")
        password = formin.cleaned_data.get("password")
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.activated:
                return HttpResponseRedirect('/user/student_details')
            else:
                return HttpResponseRedirect('/home/personal_info/')
    context={"form":form, "formin":formin}
    return render(request,'home/index.html',context)


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

def personal_info(request):
    interestForm = interestModel(request.POST or None)
    formInfo = StudentInfo(request.POST or None, request.FILES or None)
    formDefault = defaultForm(request.POST or None, request.FILES or None)
    if formInfo.is_valid() and formDefault.is_valid() and interestForm.is_valid():
        request.user.location = formDefault.cleaned_data.get("location")
        request.user.dob = formDefault.cleaned_data.get("dob")
        request.user.profile_picture = formDefault.cleaned_data.get("profile_picture")
        request.user.activated = True
        request.user.save()
        user_info = student_detail(email=request.user, )
        user_info.label = request.user.email
        user_info.college = formInfo.cleaned_data.get("college")
        user_info.year = formInfo.cleaned_data.get("year")
        user_info.degree = formInfo.cleaned_data.get("degree")
        user_info.save()
        user_interest = interests(email=request.user, )
        user_interest.label = request.user.email
        user_interest.marketing = interestForm.cleaned_data.get("marketing")
        user_interest.finance = interestForm.cleaned_data.get("finance")
        user_interest.public_relations = interestForm.cleaned_data.get("public_relations")
        user_interest.human_resources = interestForm.cleaned_data.get("human_resources")
        user_interest.ent_dev = interestForm.cleaned_data.get("ent_dev")
        user_interest.business_quiz = interestForm.cleaned_data.get("business_quiz")
        user_interest.save()
        return HttpResponseRedirect('/profile_page/')
    context = {"formInfo":formInfo, "interest":interestForm, "default":formDefault}
    return render(request,'home/new_studentsetup.html',context)
