from django.shortcuts import render
from users.models import colleges,student_detail, events
# Create your views here.
def dashboard(request):
    return render(request,'student_dash/events_feed.html','')