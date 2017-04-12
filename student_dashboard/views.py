from django.shortcuts import render
from users.models import colleges,student_detail, events
# Create your views here.
def dashboard(request):
    all_event = events.objects.get.all()
    event =  events.objects.get.filter(name = 'Revamp')
    x = event.colleges.college_name
    return render(request,'student_dash/events_feed.html','')