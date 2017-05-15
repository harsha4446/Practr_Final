from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table, clubs, register_table, rounds, event_registered,student, round_scores
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .forms import dataForm


# Create your views here.


def dashboard(request):
    current_user = request.user
    all_rounds = None
    form = dataForm(request.POST or None, request.FILES or None)
    try:
         register = event_registered.objects.get(current_user = current_user)
         registered = register.registered_to.all()
         for x in registered:
             round = rounds.objects.filter(email = x, published=True)
             if all_rounds is None:
                 all_rounds = round
             else:
                 all_rounds = all_rounds | round
    except event_registered.DoesNotExist:
        registered = None
        return render(request, 'student_dash/noEvent.html', {'user': current_user})
    except rounds.DoesNotExist:
        round = None
    context = {"rounds":all_rounds, "user":current_user, "form":form }
    return render(request, 'student_dash/dashboard.html', context)


def clubs_view(request):
    user = request.user
    my_clubs = None
    try:
        college = colleges.objects.get(college_name=user.student_detail.college)
        my_clubs = clubs.objects.filter(email=college)
    except colleges.DoesNotExist:
        college = None
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
    except register_table.DoesNotExist:
        all_events = None
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


def upload_files(request,id):
    user = request.user
    round = rounds.objects.get(id = id)
    try:
        scores = round_scores.objects.get(student=user, round=round)
    except round_scores.DoesNotExist:
        scores = round_scores(student=user, round=round)
    print("something")
    if request.FILES.get("file1"):
        print("we're IN here")
        scores.data1 = request.FILES.get("file1")
    if request.POST.get("file2"):
        scores.data2 = request.FILES.get("file2")
    if request.POST.get("file3"):
        scores.data3 = request.FILES.get("file3")
    scores.submitted = True
    scores.save()
    return HttpResponseRedirect("/user/student_dashboard")