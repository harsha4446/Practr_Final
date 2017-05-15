from django.shortcuts import render
from users.models import event_registered, judge_detail, rounds, events, round_scores, student

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
    #detail = judge_detail.od)
    judging = student.objects.get(id=pk)
    scores = round_scores.objects.get(student=judging)
    round = rounds.objects.get(id=scores.round.id)
    context = {'user':user,'round':round,'scores':scores}
    return render(request,'judge_dash/assessment_form.html',context)