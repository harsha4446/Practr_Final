from django.shortcuts import render
from users.models import clubs, events, student,colleges, rounds, register_table,student, student_scores, event_registered, round_room, room_judge, round_scores, event_registered_details,sub_head, judge_detail,teams
from . forms import addEvent, addRound, rooms, deadlines, newJudge
from django.http import HttpResponseRedirect

# Create your views here.


def updateScores(scores):
    for object in scores:
        studentscore, created = student_scores.objects.get_or_create(username=object.student)
        multiplier = rounds.objects.get(id=object.round.id)
        multiplier = multiplier.weight
        studentscore.creativity = studentscore.creativity +  (multiplier*object.creativity)
        studentscore.content = studentscore.content +(multiplier * object.content)
        studentscore.presentation =studentscore.presentation + (multiplier * object.presentation)
        studentscore.rebuttal = studentscore.rebuttal + (multiplier * object.rebuttal)
        studentscore.communication = studentscore.communication + (multiplier * object.communication)
        studentscore.feasibility = studentscore.feasibility + (multiplier * object.feasibility)
        studentscore.save()


def percentage(x,total):
    if x != 0:
        return int((x/total)*100)
    else:
        return 0


def dashboard(request,core1='1',core2='2'):
    user = request.user
    if not user.club or user.judge:
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
        registered = event_registered_details.objects.filter(event=event).order_by('-id')[:10]
        marketingcount = event_registered.objects.filter(registered_to=event, registered_to__event_registered_details__marketing=True).count()
        financecount = event_registered.objects.filter(registered_to=event, registered_to__event_registered_details__finance=True).count()
        prcount = event_registered.objects.filter(registered_to=event, registered_to__event_registered_details__public_relations=True).count()
        hrcount = event_registered.objects.filter(registered_to=event,registered_to__event_registered_details__human_resources=True).count()
        edcount = event_registered.objects.filter(registered_to=event,registered_to__event_registered_details__ent_dev=True).count()
        bmcount = event_registered.objects.filter(registered_to=event,registered_to__event_registered_details__best_manager=True).count()
        total =  marketingcount+financecount+prcount+hrcount+edcount+bmcount
        marketingcount = percentage(marketingcount,total)
        financecount = percentage(financecount, total)
        prcount = percentage(prcount, total)
        hrcount = percentage(hrcount, total)
        edcount = percentage(edcount, total)
        bmcount = percentage(bmcount, total)
        print(total)
    except events.DoesNotExist:
        context= {"user":user, "club":club,}
        return render(request,'club_dash/noEvent.html',context)
    table1 = round_scores.objects.filter(round__email=event, round__type=1)
    table2 = round_scores.objects.filter(round__email=event, round__type=2)

    if core1 != '1' or core2 != '2':
        if core1 == '1':
            table1 = round_scores.objects.filter(round__email=event, round__type=1)
        if core1 == '2':
            table1 = round_scores.objects.filter(round__email=event, round__type=2)
        if core1 == '3':
            table1 = round_scores.objects.filter(round__email=event, round__type=3)
        if core1 == '4':
            table1 = round_scores.objects.filter(round__email=event, round__type=4)
        if core1 == '5':
            table1 = round_scores.objects.filter(round__email=event, round__type=5)
        if core1 == '6':
            table1 = round_scores.objects.filter(round__email=event, round__type=6)
        if core2 == '1':
            table2 = round_scores.objects.filter(round__email=event, round__type=1)
        if core2 == '2':
            table2 = round_scores.objects.filter(round__email=event, round__type=2)
        if core2 == '3':
            table2 = round_scores.objects.filter(round__email=event, round__type=3)
        if core2 == '4':
            table2 = round_scores.objects.filter(round__email=event, round__type=4)
        if core2 == '5':
            table2 = round_scores.objects.filter(round__email=event, round__type=5)
        if core2 == '6':
            table2 = round_scores.objects.filter(round__email=event, round__type=6)

    context = {"user":user, "event":event, "club":club,'count1':count1, 'count2':count2, 'count3':count3, 'count4':count4,
               'count5':count5, 'count6':count6,'registered':registered,'table1':table1,'table2':table2,
               'core1':core1,'core2':core2,'marketingcount':marketingcount,'financecount':financecount,
               'prcount':prcount,'hrcount':hrcount,'edcount':edcount,'bmcount':bmcount}
    return render(request,'club_dash/dashboard.html',context)


def live(request, id):
    event = events.objects.get(id=id)
    if event.live:
        event.live = False
        event.current = False
        event.delete()
    else:
        event.live = True
        event.current = True
        event.save()
    return HttpResponseRedirect("/user/club_dashboard/")


def activate_registraion(request, id):
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
        if request.POST.get("multi") != None:
            event.multiregistration = True
        if access == 1:
            event.inter_type = True
        event.marketing = form.cleaned_data.get("marketing")
        event.finance = form.cleaned_data.get("finance")
        event.public_relations = form.cleaned_data.get("public_relations")
        event.human_resources = form.cleaned_data.get("human_resources")
        event.ent_dev = form.cleaned_data.get("ent_dev")
        event.best_manager = form.cleaned_data.get("best_manager")
        event.firstyear = request.POST.get("first",False)
        event.secondyear = request.POST.get("second",False)
        event.thirdyear = request.POST.get("third",False)
        if not event.firstyear:
            event.quota11 = 0
            event.quota21 = 0
            event.quota31 = 0
            event.quota41 = 0
            event.quota51 = 0
            event.quota61 = 0
        if not event.secondyear:
            event.quota12 = 0
            event.quota22 = 0
            event.quota32 = 0
            event.quota42 = 0
            event.quota52 = 0
            event.quota62 = 0
        if not event.thirdyear:
            event.quota13 = 0
            event.quota23 = 0
            event.quota33 = 0
            event.quota43 = 0
            event.quota53 = 0
            event.quota63 = 0
        if request.POST.get("solo",False) != None:
            event.team_size1 = event.team_size2 = event.team_size3 = event.team_size4 = event.team_size5 = event.team_size6 = 1
        else:
            event.team_size1 = event.team_size2 = event.team_size3 = event.team_size4 = event.team_size5 = event.team_size6 = request.POST.get("team")
        if form.cleaned_data.get("logo"):
            event.logo = form.cleaned_data.get("logo")
        event.current = True
        event.save()
        return HttpResponseRedirect("/user/club_dashboard")
    context = {"form":form, "user":request.user}
    return render(request,'club_dash/add_event.html',context)


def add_round(request, id=None, operation=None, offline=None):
    if request.user.judge:
        details = judge_detail.objects.get(email=request.user)
        club = clubs.objects.get(id=details.club.id)
    else:
        club = clubs.objects.get(club_email = request.user.email)
    event = events.objects.get(id=id)
    round = rounds(email = event)
    form = addRound(request.POST or None)
    if form.is_valid():
        round.title = form.cleaned_data.get("title")
        round.sub_title = form.cleaned_data.get("sub_title")
        if request.POST.get("low"):
            round.weight = 0.33
        if request.POST.get("medium"):
            round.weight = 0.66
        if request.POST.get("high"):
            round.weight = 1.0
        round.club = club
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
        round.core1 = form.cleaned_data.get("core1")
        round.core2 = form.cleaned_data.get("core2")
        round.core3 = form.cleaned_data.get("core3")
        round.core4 = form.cleaned_data.get("core4")
        round.core5 = form.cleaned_data.get("core5")
        round.core6 = form.cleaned_data.get("core6")
        round.creativityvalue = request.POST.get("creativityvalue",0)
        round.contentvalue = request.POST.get("contentvalue",0)
        round.presentationvalue = request.POST.get("presentationvalue",0)
        round.rebuttalvalue = request.POST.get("rebuttalvalue",0)
        round.communicationvalue = request.POST.get("communicationvalue",0)
        round.feasibilityvalue = request.POST.get("feasibilityvalue",0)
        round.type = operation
        round.author = request.user.name
        round.offline = offline
        round.save()
        return HttpResponseRedirect("/user/club_dashboard/caseView/"+id+"/"+operation)
    context = {"form":form, "offline":offline}
    return render (request,'club_dash/add_round.html',context)


def del_round(request, id = None):
    round = rounds.objects.get(id=id)
    event = str (round.email.id)
    type = str (round.type)
    round.delete()
    return HttpResponseRedirect("/user/club_dashboard/caseView/"+event+"/"+type)


def case_view(request, id, type):
    event = events.objects.get(id=id)
    all_rounds = rounds.objects.filter(email=event,type=type)
    roomForm = rooms(request.POST or None)
    deadlineForm = deadlines(request.POST or None)
    judgeForm = newJudge(request.POST or None)
    register = 0
    all_rooms = None
    corename=''
    try:
        if type == '1':
            register = event_registered_details.objects.filter(event=event,marketing=True).count()
            corename = 'Marketing'
        elif type == '2':
            register = event_registered_details.objects.filter(event=event, finance=True).count()
            corename = 'Finance'
        elif type == '3':
            register = event_registered_details.objects.filter(event=event, public_relations=True).count()
            corename = 'Public Relations'
        elif type == '4':
            register = event_registered_details.objects.filter(event=event, human_resources=True).count()
            corename = 'Human Resources'
        elif type == '5':
            register = event_registered_details.objects.filter(event=event, ent_dev=True).count()
            corename = 'Entrepreneurship Development'
        elif type == '6':
            register = event_registered_details.objects.filter(event=event, best_manager=True).count()
            corename = 'Best Manager'
        all_rooms = round_room.objects.all()
    except register_table.DoesNotExist:
        register = 0
    context = {'all_rounds':all_rounds, 'user':request.user, 'event':id, 'type':type, 'count':register, 'roomForm':roomForm,
               'deadline':deadlineForm, 'all_rooms':all_rooms, 'judgeForm':judgeForm,'corename':corename}
    return render(request,'club_dash/case_view.html',context)


def publish(request, id=None, event=None, type=None):
    round = rounds.objects.get(id=id)
    if round.published:
        round.published = False
        round.deadline = None
    else:
        if request.POST:
            round.published = True
            temp = request.POST['deadline']
            round.deadline = request.POST['deadline']
    round.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/'+event+'/'+type)


def members(request, id, type):
    current_user = request.user
    round = rounds.objects.get(id=id)
    audience = None
    if round.finished:
        audience = round_scores.objects.filter(round=round,submitted=True)
    else:
        if type == '1':
            audience = event_registered_details.objects.filter(event=round.email,marketing=True)
        if type == '2':
            audience = event_registered_details.objects.filter(event=round.email,finance=True)
        if type == '3':
            audience = event_registered_details.objects.filter(event=round.email,public_relations=True)
        if type == '4':
            audience = event_registered_details.objects.filter(event=round.email,human_resources=True)
        if type == '5':
            audience = event_registered_details.objects.filter(event=round.email,ent_dev=True)
        if type == '6':
            audience = event_registered_details.objects.filter(event=round.email,best_manager=True)
    context = {'user':current_user, 'audience':audience}
    return render(request,'club_dash/members.html',context)


def result(request, round=None):
    user = request.user
    round = rounds.objects.get(id=round)
    event = round.email.id
    type = round.type
    scores = round_scores.objects.filter(round=round).order_by('-total')
    count = round_scores.objects.filter(round=round).count()
    context = {'user': user, 'round':round, 'scores':scores,'event':event,'type':type,'max':count}
    return render(request, 'club_dash/results.html', context)


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


def teamSize(request, id, event,type):
    round = rounds.objects.get(id=id)
    round.team_size = request.POST.get('team_size')
    round.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/'+event+'/'+type)


def audience(request, event,type):
    id = request.POST.get("case_id")
    round = rounds.objects.get(id=id)
    #round.enddate = str (datetime.date.today)
    round.finished = True
    if round.qualified == 0:
        parameter = round_scores.objects.filter(round=round)
        updateScores(parameter)
    round.qualified = request.POST.get("qualified")
    round.save()
    mainevent = events.objects.get(id=event)
    qualify = int (round.qualified)
    reset = round_scores.objects.filter(round=round)
    for userr in reset:
        userr.qualified = False
        userr.save()
    qualified = round_scores.objects.filter(round=round).order_by('-total')[:qualify]
    print(qualified)
    for userq in qualified:
        userq.qualified = True
        userq.save()
        obj = event_registered_details.objects.get(student=userq.student, event=mainevent)
        if type == '1':
            obj.marketing = True
        if type == '2':
            obj.finance = True
        if type == '3':
            obj.public_relations = True
        if type == '4':
            obj.human_resources = True
        if type == '5':
            obj.ent_dev = True
        if type == '6':
            obj.best_manager = True
        obj.save()
    disqualified = round_scores.objects.filter(round=round, qualified=False)
    print(disqualified)
    for userd in disqualified:
        userd.qualified = False
        userd.save()
        obj = event_registered_details.objects.get(student=userd.student, event=mainevent)
        if type == '1':
            obj.marketing = False
        if type == '2':
            obj.finance = False
        if type == '3':
            obj.public_relations = False
        if type == '4':
            obj.human_resources = False
        if type == '5':
            obj.ent_dev = False
        if type == '6':
            obj.best_manager = False
        obj.save()
    return HttpResponseRedirect('/user/club_dashboard/caseView/' + event + '/' + type)


def addSub(request,id,type):
    event = events.objects.get(id=id)
    username = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    head = student.objects.create_user(email=username,password=password,phoneno=phone,name=name)
    head.club = True
    head.judge = True
    head.save()
    set_type = judge_detail(email=head)
    set_type.type = type
    club = clubs.objects.get(club_email=request.user.email)
    set_type.club = club
    set_type.save()
    details = sub_head(student=head,type=type)
    details.save()
    if type == '1':
        event.subhead1 = True
    if type == '2':
        event.subhead2 = True
    if type == '3':
        event.subhead3 = True
    if type == '4':
        event.subhead4 = True
    if type == '5':
        event.subhead5 = True
    if type == '6':
        event.subhead6 = True
    event.save()
    return HttpResponseRedirect("/user/club_dashboard/")


def quotaset(request,id=None):
    event = events.objects.get(id=id)
    event.quota11 = request.POST.get("quota11",0)
    event.quota21 = request.POST.get("quota21",0)
    event.quota31 = request.POST.get("quota31",0)
    event.quota41 = request.POST.get("quota41",0)
    event.quota51 = request.POST.get("quota51",0)
    event.quota61 = request.POST.get("quota61",0)
    event.quota12 = request.POST.get("quota12",0)
    event.quota22 = request.POST.get("quota22",0)
    event.quota32 = request.POST.get("quota32",0)
    event.quota42 = request.POST.get("quota42",0)
    event.quota52 = request.POST.get("quota52",0)
    event.quota62 = request.POST.get("quota62",0)
    event.quota13 = request.POST.get("quota13",0)
    event.quota23 = request.POST.get("quota23",0)
    event.quota33 = request.POST.get("quota33",0)
    event.quota43 = request.POST.get("quota43",0)
    event.quota53 = request.POST.get("quota53",0)
    event.quota63 = request.POST.get("quota63",0)
    event.prefix = request.POST.get("prefix",'')
    event.prefix = event.prefix.upper()
    event.save()
    return HttpResponseRedirect("/user/club_dashboard/")


def registered_members(request,id):
    user = request.user
    event = events.objects.get(id=id)
    registered = event_registered_details.objects.filter(event=event).order_by('-id')
    context = {'user':user,'registered':registered}
    return render(request, 'club_dash/registeredmembers.html',context)


def master_table(request, type):
    user = request.user
    club = clubs.objects.get(club_email=user.email)
    event = events.objects.get(email=club, current=True)
    type = int (type)
    registered = round_scores.objects.filter(round__email=event, round__type=type)
    total = registered.count()
    cases = rounds.objects.filter(email=event,type=type,published=True,finished=False)
    context ={'user':user,'registered':registered,'max':total,'cases':cases,'event':event,'type':type}
    return render(request,'club_dash/audience_master.html',context)


def teamCreate(request, id, type, size):
    event = events.objects.get(id=id)
    type = int (type)
    registered = None
    if type == 1:
        registered = event_registered_details.objects.filter(event=event,marketing=True)
    if type == 2:
        registered = event_registered_details.objects.filter(event=event,finance=True)
    if type == 3:
        registered = event_registered_details.objects.filter(event=event,public_relations=True)
    if type == 4:
        registered = event_registered_details.objects.filter(event=event,human_resources=True)
    if type == 5:
        registered = event_registered_details.objects.filter(event=event,ent_dev=True)
    if type == 6:
        registered = event_registered_details.objects.filter(event=event,best_manager=True)
    firstmember = None
    secondmember = None
    thirdmember = None
    for student in registered:
        if student.student.student_detail.year == 'First':
            if firstmember == None:
                firstmember = student
            else:
                firstmember = firstmember | student
        elif student.student.student_detail.year == 'Second':
            if secondmember == None:
                secondmember = student
            else:
                secondmember = secondmember | student
        elif student.student.student_detail.year == 'Third':
            if thirdmember == None:
                thirdmember = student
            else:
                thirdmember = thirdmember | student
    while 1:
        if len(firstmember) > len(secondmember):
            temp = firstmember
            firstmember = secondmember
            secondmember = temp
        if len(secondmember) > len(thirdmember):
            temp = secondmember
            secondmember = thirdmember
            thirdmember = temp
        if len(firstmember) >= len(secondmember) >= len(thirdmember):
            break

    for first in firstmember:
        team = teams(event=event,type=type)
        team.member1 = first
        for second in secondmember:
            team.member2 = second
            #if thirdmember is none, skip and make member 3 = object from member2
            for third in thirdmember:
                team.member3 = third
                if third in thirdmember:
                    thirdmember.remove(third)
                break
            if second in secondmember:
                thirdmember.remove(second)
            break
        if first in firstmember:
            firstmember.remove(first)
        break
