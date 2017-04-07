from django.shortcuts import render
from users.models import clubs, events, colleges
from . forms import openRegistarion

# Create your views here.
def dashboard(request):
    user = request.user
    club = clubs.objects.get(club_email=user.email)
    #college = colleges(email = user)
    open = openRegistarion(request.POST or None)
    all_event = events.objects.filter(email = club)
    context = {"user":user, "all_events":all_event, "club":club,"open":open}
    return render(request,'club_dash/dashboard.html',context)