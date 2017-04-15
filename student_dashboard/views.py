from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table
# Create your views here.



def dashboard(request):
    current_user = request.user
    try:
        follow = follow_table.objects.get(current_user = current_user)
        all_events = events.objects.all()
    except follow.DoesNotExist:
        follow = None
    except all_events.DoesNotExist:
        all_events = None
    friend_requests = follow.connected_to.all()
    print(friend_requests)
    context = {"requests":friend_requests, "user":current_user, "events":all_events, }
    return render(request,'student_dash/events_feed.html',context)