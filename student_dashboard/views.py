from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table, clubs, register_table
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# Create your views here.



def dashboard(request):
    current_user = request.user
    try:
         follow = follow_table.objects.get(current_user = current_user)
         friend_requests = follow.connected_to.all()
    except follow_table.DoesNotExist:
        friend_requests = None
    all_events  = events.objects.filter()
    context = {"requests":friend_requests, "user":current_user, "events":all_events, }
    return render(request, 'student_dash/dashboard.html', context)


def clubs_view(request):
    user = request.user
    college = colleges.objects.get(college_name=user.student_detail.college)
    my_clubs = clubs.objects.filter(email=college)
    all_clubs = clubs.objects.all()
    x = all_clubs.first()
    print(x.logo.url)
    context = {"user":user , "my_clubs":my_clubs, "all_clubs":all_clubs}
    return render(request, 'student_dash/clubs_view.html', context)

def club_register(request, id = None):
    current_user = request.user
    club = clubs.objects.get(id=id)
    register_table.register(current_user,club)
    return HttpResponseRedirect("/user/student_dashboard/clubs")