from django.shortcuts import render
from . models import student, interests, student_detail, judge_detail,colleges, clubs
from .forms import RegisterModel,LoginForm, StudentInfo, JudgeInfo, interestModel, defaultForm, newClub,newCollege
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
                return HttpResponseRedirect('/user/club_dashboard')
            else:
                return HttpResponseRedirect('/home/newstudent_info/')
    context={"form":form, "formin":formin}
    return render(request,'home/index.html',context)


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

def new_student(request):
    if request.user.judge:
        return HttpResponseRedirect('/home/newjudge_info/')
    if request.user.college:
        return HttpResponseRedirect('/home/newcollege_info/')
    interestForm = interestModel(request.POST or None)
    formInfo = StudentInfo(request.POST or None)
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
        user_info.industry_exp = formInfo.cleaned_data.get("industry_exp")
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
    context = {"formInfo":formInfo, "interest":interestForm, "default":formDefault, "user":request.user,}
    return render(request,'home/new_studentsetup.html',context)


def new_judge(request):
    if not request.user.judge:
        return HttpResponseRedirect('/home/newstudent_info/')
    if request.user.college:
        return HttpResponseRedirect('/home/newcollege_info/')
    interestForm = interestModel(request.POST or None)
    formInfo = JudgeInfo(request.POST or None)
    formDefault = defaultForm(request.POST or None, request.FILES or None)
    if formDefault.is_valid() and formInfo.is_valid() and  interestForm.is_valid():
        request.user.location = formDefault.cleaned_data.get("location")
        request.user.dob = formDefault.cleaned_data.get("dob")
        request.user.profile_picture = formDefault.cleaned_data.get("profile_picture")
        request.user.activated = True
        request.user.save()
        user_info = judge_detail(email=request.user, )
        user_info.label = request.user.email
        user_info.degree = formInfo.cleaned_data.get("degree")
        user_info.website = formInfo.cleaned_data.get("website")
        user_info.industry_exp = formInfo.cleaned_data.get("industry_exp")
        user_info.college = formInfo.cleaned_data.get("college")
        user_info.designation = formInfo.cleaned_data.get("designation")
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
        return HttpResponseRedirect('/judge_dashboard/')
    context = {"formInfo": formInfo, "interest": interestForm, "default": formDefault, "user":request.user,}
    return render(request, 'home/new_judge.html', context)


def new_college(request):
    if not request.user.college:
        return HttpResponseRedirect('/home/newstudent_info/')
    formCollege = newCollege(request.POST or None)
    formClub = newClub(request.POST or None)
    if formCollege.is_valid() and formClub.is_valid():
        college = colleges(email=request.user)
        college.college_name = formCollege.cleaned_data.get("college_name")
        college.address = formCollege.cleaned_data.get("address")
        college.phone = formCollege.cleaned_data.get("phone")
        college.save()
        request.user.activated= True
        request.user.save()
        club = clubs(email=college)
        club.name = formClub.cleaned_data.get("name")
        club.admin_name = formClub.cleaned_data.get("admin_name")
        club_password = formClub.cleaned_data.get("club_password")
        club.phone = formClub.cleaned_data.get("phone")
        club.club_email = formClub.cleaned_data.get("club_email")
        new_user = User.objects.create_user(club.club_email, club_password, club.admin_name, club.phone)
        new_user.club=True
        new_user.save()
        club.save()
        college = colleges(email = club)
        college.save()
        return HttpResponseRedirect('/college_dashboard/')

    context = {"college":formCollege, "club":formClub,}
    return render (request, 'home/new_college.html', context)



