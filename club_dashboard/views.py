from django.shortcuts import render
from users.models import clubs, events, colleges
from . forms import openRegistarion, addEvent
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
    context = {"user":user, "all_events":all_event, "club":club,"open":open}
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
    form = addEvent(request.POST or None)
    if form.is_valid():
        event = events(email=club)
        event.name = form.cleaned_data.get("name")
        event.about = form.cleaned_data.get("about")
        event.website = form.cleaned_data.get("website")
        event.save()
        return HttpResponseRedirect("/user/club_dashboard")
    context = {"form":form, "user":request.user}
    return render(request,'club_dash/add_event.html',context)