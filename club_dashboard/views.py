from django.shortcuts import render
from users.models import clubs, events, colleges, rounds, register_table,student, event_registered, round_scores
from . forms import openRegistarion, addEvent, addRound, scoreForm
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
    open = openRegistarion(request.POST or None)
    all_event = events.objects.filter(email = club)
    context = {"user":user, "events":all_event, "club":club,"open":open,}
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
    form = addEvent(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = events(email=club)
        event.name = form.cleaned_data.get("name")
        event.about = form.cleaned_data.get("about")
        event.website = form.cleaned_data.get("website")
        event.inter_type = form.cleaned_data.get("inter_type")
        event.team_size = form.cleaned_data.get("team_size")
        event.marketing = form.cleaned_data.get("marketing")
        event.finance = form.cleaned_data.get("finance")
        event.public_relations = form.cleaned_data.get("public_relations")
        event.human_resources = form.cleaned_data.get("human_resources")
        event.ent_dev = form.cleaned_data.get("ent_dev")
        event.business_quiz = form.cleaned_data.get("business_quiz")
        if form.cleaned_data.get("logo"):
            event.logo = form.cleaned_data.get("logo")
        event.save()
        return HttpResponseRedirect("/user/club_dashboard")
    context = {"form":form, "user":request.user}
    return render(request,'club_dash/add_event.html',context)


def sub_events(request, id = None):
    event = events.objects.get(id = id)
    user = request.user
    count1 = rounds.objects.filter(email=event, type=1).count()
    count2 = rounds.objects.filter(email=event, type=2).count()
    count3 = rounds.objects.filter(email=event, type=3).count()
    count4 = rounds.objects.filter(email=event, type=4).count()
    count5 = rounds.objects.filter(email=event, type=5).count()
    count6 = rounds.objects.filter(email=event, type=6).count()
    context = {'event':event, 'user':user, 'count1':count1, 'count2':count2, 'count3':count3, 'count4':count4,
               'count5':count5, 'count6':count6,}
    return render(request,'club_dash/sub_events.html',context)


def add_round(request, id=None, operation=None):
    club = clubs.objects.get(club_email = request.user.email)
    event = events.objects.get(id=id)
    round = rounds(email = event)
    form = addRound(request.POST or None)
    if form.is_valid():
        round.title = form.cleaned_data.get("title")
        round.sub_title = form.cleaned_data.get("sub_title")
        round.about = form.cleaned_data.get("sub_title")
        round.task1 = form.cleaned_data.get("task1")
        round.task2 = form.cleaned_data.get("task2")
        round.task3 = form.cleaned_data.get("task3")
        round.task4 = form.cleaned_data.get("task4")
        round.task5 = form.cleaned_data.get("task5")
        round.resource1 = form.cleaned_data.get("resource1")
        round.resource2 = form.cleaned_data.get("resource2")
        round.resource3 = form.cleaned_data.get("resource3")
        round.resource4 = form.cleaned_data.get("resource4")
        round.resource5 = form.cleaned_data.get("resource5")
        round.ext_judge = form.cleaned_data.get("ext_judge")
        round.creativity = form.cleaned_data.get("creativity")
        round.content = form.cleaned_data.get("content")
        round.presentation = form.cleaned_data.get("presentation")
        round.rebuttal = form.cleaned_data.get("rebuttal")
        round.communication = form.cleaned_data.get("communication")
        round.feasibility = form.cleaned_data.get("feasibility")
        round.feedback = form.cleaned_data.get("feedback")
        round.question1 = form.cleaned_data.get("question1")
        round.question2 = form.cleaned_data.get("question2")
        round.question3 = form.cleaned_data.get("question3")
        round.question4 = form.cleaned_data.get("question4")
        round.question5 = form.cleaned_data.get("question5")
        round.type = operation
        round.save()
        return HttpResponseRedirect("/user/club_dashboard/subEvents/"+id)
    context = {"form":form,}
    return render (request,'club_dash/add_round.html',context)


def del_event(request, id = None):
    event = events.objects.get(id = id)
    event.delete()
    return HttpResponseRedirect("/user/club_dashboard")


def case_view(request, id, type):
    event = events.objects.get(id=id)
    all_rounds = rounds.objects.filter(email=event,type=type)
    register = 0
    try:
        club = clubs.objects.get(club_email=request.user.email)
        register = register_table.objects.filter(registered_to=club).count()
    except register_table.DoesNotExist:
        register = 0
    context = {'all_rounds':all_rounds, 'user':request.user, 'event':id, 'type':type, 'count':register}
    return render(request,'club_dash/case_view.html',context)


def publish(request, id, event, type):
    round = rounds.objects.get(id=id)
    if round.published:
        round.published = False
    else:
        round.published = True
    round.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/'+event+'/'+type)


def members(request):
    current_user = request.user
    students= None
    try:
        studen = register_table.objects.get(current_user = current_user)
        students = studen.registered_to.all()
    except register_table.DoesNotExist:
        studen = None
    print (students)
    context = {'user':current_user, 'students':students}
    return render(request,'club_dash/members.html',context)


def judge_list(request, id=None, round=None):
    user = request.user
    event = events.objects.get(id=id)
    registered = None
    try:
        registered = event_registered.objects.filter(registered_to=event)
    except event_registered.DoesNotExist:
        registered = None
    context = {'user': user, 'registered':registered, 'event':event, 'round':round}
    return render(request, 'club_dash/judge_selection.html', context)


def judge(request, id=None,student_id=None,event=None):
    Student = student.objects.get(id=student_id)
    round = rounds.objects.get(id=id)
    scores = round_scores(round=round,student=Student)
    form = scoreForm(request.POST or None)
    if form.is_valid:
        scores.question1 = form.cleaned_data.get('question1')
        scores.question2 = form.cleaned_data.get('question2')
        scores.question3 = form.cleaned_data.get('question3')
        scores.question4 = form.cleaned_data.get('question4')
        scores.question5 = form.cleaned_data.get('question5')
        scores.feedback = form.cleaned_data.get('feedback')
        if round.feasibility:
            scores.feasibility = form.cleaned_data.get('feasibility')
        if round.communication:
            scores.communication = form.cleaned_data.get('communication')
        if round.content:
            scores.content = form.cleaned_data.get('content')
        if round.creativity:
            scores.creativity = form.cleaned_data.get('creativity')
        if round.rebuttal:
            scores.rebuttal = form.cleaned_data.get('rebuttal')
        scores.save()
        return HttpResponseRedirect('/user/club_dashboard/judge_list/'+event)
    context = {'form':form}
    return render (request, '', context)


