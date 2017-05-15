from django.shortcuts import render
from users.models import clubs, events, colleges, rounds, register_table,student, event_registered, round_room, room_judge, round_scores
from . forms import addEvent, addRound, scoreForm, toggles, rooms, deadlines, newJudge
from django.http import HttpResponseRedirect

# Create your views here.


def dashboard(request):
    user = request.user
    form = toggles(request.POST or None)
    if not user.club:
        if user.college:
            return HttpResponseRedirect("/user/college_dashboard/")
        if user.judge:
            return HttpResponseRedirect("/user/judge_dashboard/")
        return HttpResponseRedirect("/user/student_dashboard/")
    user = request.user
    club = clubs.objects.get(club_email=user.email)
    try:
        event = events.objects.get(email = club, current = True)
        count1 = rounds.objects.filter(email=event, type=1).count()
        count2 = rounds.objects.filter(email=event, type=2).count()
        count3 = rounds.objects.filter(email=event, type=3).count()
        count4 = rounds.objects.filter(email=event, type=4).count()
        count5 = rounds.objects.filter(email=event, type=5).count()
        count6 = rounds.objects.filter(email=event, type=6).count()
        form.active = event.registration
        form.live = event.live
    except events.DoesNotExist:
        context= {"user":user, "club":club,}
        return render(request,'club_dash/noEvent.html',context)

    if form.is_valid():
        print("adsfasdfasdljkfhasdlkjfhasd")
        if request.POST.get('live'):
            event.live = request.POST.get('live')
        if request.POST.get('active'):
            event.live = request.POST.get('active')
        event.save()
    context = {"user":user, "event":event, "club":club,'count1':count1, 'count2':count2, 'count3':count3, 'count4':count4,
               'count5':count5, 'count6':count6, 'form':form}
    return render(request,'club_dash/dashboard.html',context)


def activate(request, id):
    event = events.objects.get(id=id)
    if event.registration:
        event.registration = False
    else:
        event.registration = True
    event.save()
    return HttpResponseRedirect("/user/club_dashboard/")


def add_event(request,access = None):
    club = clubs.objects.get(club_email=request.user.email)
    form = addEvent(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = events(email=club)
        event.name = form.cleaned_data.get("name")
        event.about = form.cleaned_data.get("about")
        event.website = form.cleaned_data.get("website")
        if access == 1:
            event.inter_type = True
        event.marketing = form.cleaned_data.get("marketing")
        event.finance = form.cleaned_data.get("finance")
        event.public_relations = form.cleaned_data.get("public_relations")
        event.human_resources = form.cleaned_data.get("human_resources")
        event.ent_dev = form.cleaned_data.get("ent_dev")
        event.business_quiz = form.cleaned_data.get("best_manager")
        if form.cleaned_data.get("team_size1") != None:
            event.team_size1 = form.cleaned_data.get("team_size1")
        if form.cleaned_data.get("team_size2") != None:
            event.team_size2 = form.cleaned_data.get("team_size2")
        if form.cleaned_data.get("team_size3")!= None:
            event.team_size3 = form.cleaned_data.get("team_size3")
        if form.cleaned_data.get("team_size4")!= None:
            event.team_size4 = form.cleaned_data.get("team_size4")
        if form.cleaned_data.get("team_size5")!= None:
            event.team_size5 = form.cleaned_data.get("team_size5")
        if form.cleaned_data.get("team_size6")!= None:
            event.team_size6 = form.cleaned_data.get("team_size6")
        if form.cleaned_data.get("logo"):
            event.logo = form.cleaned_data.get("logo")
        event.current = True
        event.save()
        return HttpResponseRedirect("/user/club_dashboard")
    context = {"form":form, "user":request.user}
    return render(request,'club_dash/add_event.html',context)


def add_round(request, id=None, operation=None):
    club = clubs.objects.get(club_email = request.user.email)
    event = events.objects.get(id=id)
    round = rounds(email = event)
    form = addRound(request.POST or None)
    if form.is_valid():
        round.title = form.cleaned_data.get("title")
        round.sub_title = form.cleaned_data.get("sub_title")
        round.about = form.cleaned_data.get("about")
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
        return HttpResponseRedirect("/user/club_dashboard/")
    context = {"form":form,}
    return render (request,'club_dash/add_round.html',context)


def del_event(request, id = None):
    event = events.objects.get(id = id)
    event.delete()
    return HttpResponseRedirect("/user/club_dashboard")


def case_view(request, id, type):
    event = events.objects.get(id=id)
    all_rounds = rounds.objects.filter(email=event,type=type)
    roomForm = rooms(request.POST or None)
    deadlineForm = deadlines(request.POST or None)
    judgeForm = newJudge(request.POST or None)
    register = 0
    judges = 0
    all_rooms = None
    try:
        club = clubs.objects.get(club_email=request.user.email)
        register = register_table.objects.filter(registered_to=club).count()
        all_rooms = round_room.objects.all()
    except register_table.DoesNotExist:
        register = 0
    context = {'all_rounds':all_rounds, 'user':request.user, 'event':id, 'type':type, 'count':register, 'roomForm':roomForm,
               'deadline':deadlineForm, 'all_rooms':all_rooms, 'judgeForm':judgeForm}
    return render(request,'club_dash/case_view.html',context)


def publish(request, id=None, event=None, type=None):
    round = rounds.objects.get(id=id)
    if round.published:
        round.published = False
        round.deadline = None
    else:
        if request.POST:
            round.published = True
            round.deadline = request.POST['deadline']
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


def addRoom(request,id,event,type):
    round = rounds.objects.get(id = id)
    room = round_room(round = round)
    room.room = request.POST['room']
    room.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/'+event+'/'+type)


def addJudge(request,id,event,type):
    round = rounds.objects.get(id=id)
    room = round_room.objects.first()
    judge = room_judge(room=room, round=round)
    judge.judge_email = request.POST['judge_email']
    judge.judge_password = request.POST['judge_password']
    judge.save()
    user = student.objects.create_user(email=judge.judge_email, password=judge.judge_password, name='', phoneno='')
    user.judge = True
    user.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/' + event + '/' + type)

#Sub-Event Old
# def sub_events(request, id = None):
#     event = events.objects.get(id = id)
#     user = request.user
#     count1 = rounds.objects.filter(email=event, type=1).count()
#     count2 = rounds.objects.filter(email=event, type=2).count()
#     count3 = rounds.objects.filter(email=event, type=3).count()
#     count4 = rounds.objects.filter(email=event, type=4).count()
#     count5 = rounds.objects.filter(email=event, type=5).count()
#     count6 = rounds.objects.filter(email=event, type=6).count()
#     context = {'event':event, 'user':user, 'count1':count1, 'count2':count2, 'count3':count3, 'count4':count4,
#                'count5':count5, 'count6':count6,}
#     return render(request,'club_dash/sub_events.html',context)
