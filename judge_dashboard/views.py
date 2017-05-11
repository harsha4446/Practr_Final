from django.shortcuts import render
from users.models import event_registered, judge_detail, rounds, events

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