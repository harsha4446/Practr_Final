from django.shortcuts import render
from users.models import event_registered, judge_detail, rounds, events, round_scores, student, clubs,event_registered_details,register_table
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    user = request.user
    details = judge_detail.objects.get(email=user)
    event = events.objects.get(email=details.club, current=True)
    all_rounds = rounds.objects.filter(email=event, type=details.type)
    register = 0
    try:
        club = clubs.objects.get(id=details.club.id)
        if type == '1':
            register = event_registered_details.objects.filter(event=event, marketing=True).count()
        elif type == '2':
            register = event_registered_details.objects.filter(event=event, finance=True).count()
        elif type == '3':
            register = event_registered_details.objects.filter(event=event, public_relations=True).count()
        elif type == '4':
            register = event_registered_details.objects.filter(event=event, human_resources=True).count()
        elif type == '5':
            register = event_registered_details.objects.filter(event=event, ent_dev=True).count()
        elif type == '6':
            register = event_registered_details.objects.filter(event=event, best_manager=True).count()
    except register_table.DoesNotExist:
        register = 0
    context = {'all_rounds': all_rounds, 'user': request.user, 'event': event.id, 'type': details.type, 'count': register}
    return render(request, 'club_dash/case_view.html', context)

def judge_view(request,id):
    user = request.user
    context = {'user': user, }
    details = judge_detail.objects.get(email=user)
    round = rounds.objects.get(id=id)
    registered = None
    try:
        registered = round_scores.objects.filter(round=round,submitted=True)
    except event_registered.DoesNotExist:
        registered = None
    context = {'user': user, 'registered': registered, 'round': round.id}
    return render(request, 'judge_dash/dashboard.html', context)

def assessment(request,pk=None,id=None):
    user = request.user
    round = rounds.objects.get(id=id)
    scores = None
    if pk != '0':
        judging = student.objects.get(id=pk)
        scores = round_scores.objects.get(student=judging,round=round)
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
        scores.total = int (scores.question1)+int(scores.question2)+int(scores.question3)+int(scores.question4)+int(scores.question5)+int(scores.creativity)+int(scores.feasibility)+int(scores.content)+int(scores.communication)+int(scores.rebuttal)+int(scores.presentation)
        scores.save()
        return HttpResponseRedirect("/user/judge_dashboard")
    context = {'user':user,'round':round,'scores':scores}
    return render(request,'judge_dash/assessment_form.html',context)