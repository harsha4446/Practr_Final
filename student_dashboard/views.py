from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table, clubs, register_table, rounds, event_registered,student
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect


# Create your views here.


def dashboard(request):
    current_user = request.user
    all_rounds = None
    try:
         register = event_registered.objects.get(current_user = current_user)
         registered = register.registered_to.all()
         for x in registered:
             round = rounds.objects.get(email = x)
             all_rounds = all_rounds | round
    except event_registered.DoesNotExist:
        registered = None
    print(all_rounds)
    context = {"rounds":all_rounds, "user":current_user, }
    return render(request, 'student_dash/dashboard.html', context)


def clubs_view(request):
    user = request.user
    college = colleges.objects.get(college_name=user.student_detail.college)
    my_clubs = clubs.objects.filter(email=college)
    all_clubs = clubs.objects.all()
    context = {"user":user , "my_clubs":my_clubs, "all_clubs":all_clubs}
    return render(request, 'student_dash/clubs_view.html', context)


def club_register(request, id = None):
    current_user = request.user
    club = clubs.objects.get(id=id)
    register_table.register(current_user,club)
    return HttpResponseRedirect("/user/student_dashboard/clubs")


def event_feed(request):
    current_user = request.user
    all_events = None
    try:
        register = register_table.objects.get(current_user=current_user)
        clubs = register.registered_to.all()
        for x in clubs:
            y = events.objects.filter(email = x)
            if all_events is None:
                all_events = y
            else:
                all_events = all_events | y
    except follow_table.DoesNotExist:
        register = None
    context = { "user": current_user, "events": all_events, }
    return render(request, 'student_dash/event_feed.html', context)


def event_register(request, id = None):
    current_user = request.user
    event = events.objects.get(id=id)
    event_registered.register(current_user, event)
    return HttpResponseRedirect("/user/student_dashboard/events")


def search(request):
    all_users = student.objects.filter(judge=False, college=False, club=False)
    context = {"all_users": all_users, }
    return render(request, 'student_dash/student_list.html', context)