from django.shortcuts import render
from users.models import event_registered, judge_detail, rounds, events, round_scores, student
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    user = request.user
    context = {'user':user,}
    details = judge_detail.objects.get(email=user)
    round = rounds.objects.get(id = details.round.id)
    event = events.objects.get(id = round.email.id)
    registered = None
    try:
        registered = event_registered.objects.filter(registered_to=event)
    except event_registered.DoesNotExist:
        registered = None
    context ={'user':user,'registered':registered, 'event':event, 'round':round}
    return render(request,'judge_dash/dashboard.html',context)

def assessment(request,pk=None):
    user = request.user
    judging = student.objects.get(id=pk)
    scores = round_scores.objects.get(student=judging)
    round = rounds.objects.get(id=scores.round.id)
    if request.POST:
        scores.question1 = request.POST.get("question1")
        scores.question2 = request.POST.get("question2",0)
        scores.question3 = request.POST.get("question3",0)
        scores.question4 = request.POST.get("question4",0)
        scores.question5 = request.POST.get("question5",0)
        scores.creativity = request.POST.get("creativity1",0)
        scores.communication = request.POST.get("communication1",0)
        scores.content = request.POST.get("content1",0)
        scores.feasibility = request.POST.get("feasibility1",0)
        scores.rebuttal = request.POST.get("rebuttal1",0)
        scores.presentation = request.POST.get("presentation1",0)
        scores.feedback = request.POST.get("feedback",'')
        scores.judged = True
        scores.save()
        return HttpResponseRedirect("/user/judge_dashboard")
    context = {'user':user,'round':round,'scores':scores}
    return render(request,'judge_dash/assessment_form.html',context)