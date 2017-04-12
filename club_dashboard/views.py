from django.shortcuts import render
from users.models import clubs, events, colleges, rounds
from . forms import openRegistarion, addEvent, addRound
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    user = request.user
    if not user.club:
        if user.college:
            return HttpResponseRedirect("/user/college_dashboard/")

        return HttpResponseRedirect("/user/student_dashboard/")
    user = request.user
    club = clubs.objects.get(club_email=user.email)
    #college = colleges(email = user)
    open = openRegistarion(request.POST or None)
    all_event = events.objects.filter(email = club)
    all_rounds = rounds.objects.filter(club = club.club_email)
    context = {"user":user, "all_events":all_event, "club":club,"open":open,"all_rounds":all_rounds,}
    return render(request,'club_dash/dashboard.html',context)


def activate(request, id):
    event = events.objects.get(id=id)
    if event.registration:
        event.registration = False
    else:
        event.registration = True
    event.save()
    return HttpResponseRedirect("/user/club_dashboard/")


def add_event(request):
    club = clubs.objects.get(club_email=request.user.email)
    form = addEvent(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = events(email=club)
        event.name = form.cleaned_data.get("name")
        event.about = form.cleaned_data.get("about")
        event.website = form.cleaned_data.get("website")
        event.logo = form.cleaned_data.get("logo")
        event.inter_type = form.cleaned_data.get("inter_type")
        event.save()
        return HttpResponseRedirect("/user/club_dashboard")
    context = {"form":form, "user":request.user}
    return render(request,'club_dash/add_event.html',context)


def add_round(request, id=None):
    club = clubs.objects.get(club_email = request.user.email)
    event = events.objects.get(id=id)
    round = rounds(email = event)
    form = addRound(request.POST or None)
    if form.is_valid():
        round.club = club.club_email
        round.event = event.name
        round.title = form.cleaned_data.get("title")
        round.sub_title = form.cleaned_data.get("sub_title")
        round.about = form.cleaned_data.get("sub_title")
        round.task1 = form.cleaned_data.get("task1")
        round.task2 = form.cleaned_data.get("task2")
        round.task3 = form.cleaned_data.get("task3")
        round.task4 = form.cleaned_data.get("task4")
        round.task5 = form.cleaned_data.get("task5")
        round.resource1 = form.cleaned_data.get("resource1")
        round.resource2 = form.cleaned_data.get("resource2")
        round.resource3 = form.cleaned_data.get("resource3")
        round.resource4 = form.cleaned_data.get("resource4")
        round.resource5 = form.cleaned_data.get("resource5")
        round.ext_judge = form.cleaned_data.get("ext_judge")
        round.creativity = form.cleaned_data.get("creativity")
        round.content = form.cleaned_data.get("content")
        round.presentation = form.cleaned_data.get("presentation")
        round.rebuttal = form.cleaned_data.get("rebuttal")
        round.communication = form.cleaned_data.get("communication")
        round.feasibility = form.cleaned_data.get("feasibility")
        round.feedback = form.cleaned_data.get("feedback")
        round.question1 = form.cleaned_data.get("question1")
        round.question2 = form.cleaned_data.get("question2")
        round.question3 = form.cleaned_data.get("question3")
        round.question4 = form.cleaned_data.get("question4")
        round.question5 = form.cleaned_data.get("question5")
        #round.ext_judge = False
        round.save()
        return HttpResponseRedirect("/user/club_dashboard")
    else:
        print("not valid form")
    context = {"form":form,}
    return render (request,'club_dash/add_round.html',context)


