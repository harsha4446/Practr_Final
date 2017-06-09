from django.shortcuts import render
from . models import student, interests, student_detail, judge_detail,colleges, clubs, room_judge, rounds
from .forms import RegisterModel,LoginForm, StudentInfo, JudgeInfo, \
    interestModel, defaultForm, newClub,newCollege, clubsetup
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .models import student


# Create your views here.

def index(request):
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
    context={"form":formin}
    return render(request,'home/index.html',context)


def register(request):
    formst = RegisterModel(request.POST or None)
    formcl = RegisterModel(request.POST or None)
    formun = RegisterModel(request.POST or None)
    all_colleges = colleges.objects.filter()
    context = {"formst":formst, "formcl":formcl,"formun":formun,"all_colleges":all_colleges}
    return render(request, 'home/register.html', context)


def registerClub(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    name = request.POST.get('name')
    phoneno = request.POST.get('phoneno')
    new_user = student.objects.create_user(username, password, name, phoneno)
    new_user.club = True
    new_user.save()
    club = clubs(club_email=new_user)
    club.college = request.POST.get("college_name")
    college = colleges.objects.get(college_name=club.college)
    club.email = college
    club.save()
    return HttpResponseRedirect('/home/')


def registerStudent(request):
    username = request.POST.get('email')
    password =  request.POST.get('password')
    name =  request.POST.get('name')
    phoneno =  request.POST.get('phoneno')
    new_user = student.objects.create_user(username, password, name, phoneno)
    new_user.save()
    user_info = student_detail(email=new_user, )
    user_info.college = request.POST.get('college_name')
    user_info.save()
    return HttpResponseRedirect('/home/')


def registerUni(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    name = request.POST.get('name')
    phoneno = request.POST.get('phoneno')
    new_user = student.objects.create_user(username, password, name, phoneno)
    new_user.college = True
    new_user.save()
    return HttpResponseRedirect('/home/')


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')


def new_student(request):
    if request.user.judge:
        return HttpResponseRedirect('/home/newjudge_info/')
    if request.user.college:
        return HttpResponseRedirect('/home/newcollege_info/')
    if request.user.club:
        return HttpResponseRedirect('/home/newclub_info/')
    interestForm = interestModel(request.POST or None)
    formInfo = StudentInfo(request.POST or None)
    formDefault = defaultForm(request.POST or None, request.FILES or None)
    print("here1")
    if formInfo.is_valid() and formDefault.is_valid() and interestForm.is_valid():
        print("here2")
        request.user.location = formDefault.cleaned_data.get("location")
        request.user.dob = request.POST.get("dob")
        if formDefault.cleaned_data.get("profile_picture"):
            request.user.profile_picture = formDefault.cleaned_data.get("profile_picture")
        request.user.about = formDefault.cleaned_data.get("about")
        request.user.activated = True
        request.user.save()
        user_info,created = student_detail.objects.get_or_create(email=request.user, )
        user_info.label = request.user.email
        user_info.industry_exp = formInfo.cleaned_data.get("industry_exp")
        user_info.degree = formInfo.cleaned_data.get("degree")
        user_info.section = formInfo.cleaned_data.get("section")
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
        return HttpResponseRedirect('/user/student_dashboard')
    all_colleges = colleges.objects.filter()
    context = {"formInfo":formInfo, "interest":interestForm, "default":formDefault, "user":request.user, "all_colleges":all_colleges}
    return render(request,'home/new_studentsetup.html',context)


def new_judge(request):
    if not request.user.judge:
        if request.user.club:
            return HttpResponseRedirect('/home/newclub_info/')
        elif request.user.college:
            return HttpResponseRedirect('/home/newcollege_info/')
        else:
            return HttpResponseRedirect('/home/newstudent_info/')
    formInfo = JudgeInfo(request.POST or None)
    formDefault = defaultForm(request.POST or None, request.FILES or None)
    if formDefault.is_valid() and formInfo.is_valid():
        request.user.location = formDefault.cleaned_data.get("location")
        request.user.dob = formDefault.cleaned_data.get("dob")
        request.user.profile_picture = formDefault.cleaned_data.get("profile_picture")
        request.user.activated = True
        request.user.save()
        user_info,created = judge_detail.objects.get_or_create(email=request.user, )
        user_info.degree = formInfo.cleaned_data.get("degree")
        user_info.website = formInfo.cleaned_data.get("website")
        user_info.industry_exp = formInfo.cleaned_data.get("industry_exp")
        user_info.college = formInfo.cleaned_data.get("college")
        user_info.designation = formInfo.cleaned_data.get("designation")
        # room = room_judge.objects.get(judge_email=request.user.email)
        # round = rounds.objects.get(id = room.round.id)
        user_info.save()
        return HttpResponseRedirect('/user/judge_dashboard/')
    context = {"formInfo": formInfo, "default": formDefault, "user":request.user,}
    return render(request, 'home/new_judge.html', context)


def new_college(request):
    if not request.user.college:
        if request.user.club:
            return HttpResponseRedirect('/home/newclub_info/')
        elif request.user.judge:
            return HttpResponseRedirect('/home/newjudge_info/')
        else:
            return HttpResponseRedirect('/home/newstudent_info/')
    formCollege = newCollege(request.POST or None)
    formClub = newClub(request.POST or None)
    if formCollege.is_valid() and formClub.is_valid():
        college = colleges(email=request.user)
        college.college_name = formCollege.cleaned_data.get("college_name")
        college.address = formCollege.cleaned_data.get("address")
        if formCollege.cleaned_data.get("logo"):
            college.logo = formCollege.cleaned_data.get("logo")
        college.phone = request.user.phoneno
        college.save()
        request.user.activated= True
        request.user.save()
        club = clubs(email=college)
        club.name = formClub.cleaned_data.get("name")
        club.admin_name = formClub.cleaned_data.get("admin_name")
        club_password = formClub.cleaned_data.get("club_password")
        club.phone = formClub.cleaned_data.get("phone")
        club.club_email = formClub.cleaned_data.get("club_email")
        new_user = student.objects.create_user(club.club_email, club_password, club.admin_name, club.phone)
        new_user.club=True
        new_user.save()
        club.save()
        return HttpResponseRedirect('/user/college_dashboard/')
    context = {"college":formCollege, "club":formClub,}
    return render (request, 'home/new_college.html', context)


def new_club(request):
    if not request.user.club:
        if request.user.college:
            return HttpResponseRedirect('/home/newcollege_info/')
        elif request.user.judge:
            return HttpResponseRedirect('/home/newjudge_info/')
        else:
            return HttpResponseRedirect('/home/newstudent_info/')
    form = clubsetup(request.POST or None)
    user = request.user
    all_colleges = colleges.objects.filter()
    try:
        club = clubs.objects.get(club_email=user.email)
    except clubs.DoesNotExist:
        club = clubs(club_email=user.email)
    if form.is_valid():
        if not club.verified:
            college = colleges.objects.get(college_name=club.college)
            club.email = college
            club.name = request.POST.get("name")
            club.admin_name = user.name
            club.phone = user.phoneno
        club.video = form.cleaned_data.get("video")
        club.website = form.cleaned_data.get("website")
        club.about = form.cleaned_data.get("about")
        if form.cleaned_data.get("logo"):
            club.logo =  form.cleaned_data.get("logo")
        request.user.activated = True
        request.user.save()
        club.save()
        return HttpResponseRedirect('/user/club_dashboard/')
    context = {"form": form, "user": user, 'all_colleges':all_colleges, 'club':club}
    return render(request, 'home/new_club.html', context)
