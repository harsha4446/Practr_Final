from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table, clubs, register_table, rounds, event_registered,student, round_scores,judge_detail, event_registered_details, teams
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .forms import dataForm,detailFrom
from django.contrib import auth
import datetime

# Create your views here.


def compute(detail, event):
    details = event_registered_details.objects.get(id=detail)
    event = events.objects.get(id=event)
    if details.student.student_detail.year == 'First':
        if details.marketing:
            event.registered11 = event.registered11+1
        if details.finance:
            event.registered21 = event.registered21+1
        if details.public_relations:
            event.registered31 = event.registered31+1
        if details.human_resources:
            event.registered41 = event.registered41+1
        if details.event:
            event.registered51 = event.registered51+1
        if details.best_manager:
            event.registered61 = event.registered61+1
        event.save()
    elif details.student.student_detail.year == 'Second':
        if details.marketing:
            event.registered12 = event.registered12+1
        if details.finance:
            event.registered22 = event.registered22+1
        if details.public_relations:
            event.registered32 = event.registered32+1
        if details.human_resources:
            event.registered42 = event.registered42+1
        if details.event:
            event.registered52 = event.registered52+1
        if details.best_manager:
            event.registered62 = event.registered62+1
        event.save()
    elif details.student.student_detail.year == 'Third':
        if details.marketing:
            event.registered13 = event.registered13+1
        if details.finance:
            event.registered23 = event.registered23+1
        if details.public_relations:
            event.registered33 = event.registered33+1
        if details.human_resources:
            event.registered43 = event.registered43+1
        if details.event:
            event.registered53 = event.registered53+1
        if details.best_manager:
            event.registered63 = event.registered63+1
        event.save()
    return


def dashboard(request):
    current_user = request.user
    all_rounds = None
    form = dataForm(request.POST or None, request.FILES or None)
    round = None
    registered = None
    chart_scores = None
    chart_teams = None
    chart_rounds = None
    chart_high = None
    inter_type = False
    ping = 0
    try:
         register = event_registered.objects.get(current_user = current_user)
         registered = register.registered_to.all()
         ping = registered.count()
         for x in registered:
             detail = event_registered_details.objects.get(student=current_user, event=x,event__live=True)
             if detail.event.inter_type:
                 inter_type = True
             if detail.marketing:
                 round = rounds.objects.filter(email=x, published=True, type=1)
                 if round is None:
                     round = rounds.objects.filter(email = x, published=True, type=1)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=1)
             if detail.finance:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=2)
                 else:
                    round = round | rounds.objects.filter(email = x, published=True, type=2)
             if detail.public_relations:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=3)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=3)
             if detail.human_resources:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=4)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=4)
             if detail.ent_dev:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=5)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=5)
             if detail.best_manager:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=6)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=6)
             if detail.corp_strg:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=7)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=7)
             if detail.quiz:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=8)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=8)
             if detail.team:
                 if round is None:
                     round = rounds.objects.filter(email=x, published=True, type=9)
                 else:
                     round = round | rounds.objects.filter(email = x, published=True, type=9)
             if all_rounds is None:
                 all_rounds = round
             else:
                 all_rounds = all_rounds | round
             if inter_type:
                 chart_scores = round_scores.objects.filter(round__finished=True, round__email=x).values('rcode','total','round').distinct()
                 chart_teams = chart_scores.values('rcode').distinct()
                 chart_rounds = rounds.objects.filter(email=x, finished=True)
                 chart_high = round_scores.objects.filter(round__finished=True, round__email=x).order_by('-total')[:1]
                 for x in chart_high:
                    chart_high = x.total
         if all_rounds != None:
             for round in all_rounds:
                try:
                    exists = round_scores.objects.get(round=round,student=current_user)
                    if exists.data1 or exists.data2 or exists.data3:
                        round.flag = True
                    else:
                        round.flag = False
                except:
                    round.flag = False
    except event_registered.DoesNotExist:
        registered = None
        return render(request, 'student_dash/noEvent.html', {'user': current_user})
    except rounds.DoesNotExist:
        round = None
    rcodes = event_registered_details.objects.filter(student=current_user)
    context = {"rounds":all_rounds, "user":current_user, "form":form,'registered':registered,'rcode':rcodes,
               "chartRounds":chart_rounds,"chartScores":chart_scores,"chartTeams":chart_teams,
               "chartHigh":chart_high,"inter_type":inter_type}
    if ping == 0:
        return render(request, 'student_dash/noEvent.html', {'user': current_user})
    return render(request, 'student_dash/dashboard.html', context)
    #return render(request, 'judge_list/judge_list.html', context)


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
    details = student_detail.objects.get(email=current_user)
    try:
        all_events = events.objects.filter(current=True, registration=True, email__college=details.college,inter_type=False)
        registered, created = event_registered.objects.get_or_create(current_user=current_user)
        registered = registered.registered_to.all()
        for event in all_events:
            event.flag = True
            if event in registered:
                event.flag = False
        #For when we need to register to club first(works, KEEP THIS CODE)
        # register = register_table.objects.get(current_user=current_user)
        # clubs = register.registered_to.all()
        # for x in clubs:
        #     y = events.objects.filter(email = x, current=True, live=True, registration=True)
        #     if all_events is None:
        #         all_events = y
        #     else:
        #         all_events = all_events | y
    except register_table.DoesNotExist:
        all_events = None
    context = { "user": current_user, "events": all_events}
    return render(request, 'student_dash/event_feed.html', context)


def event_register(request, id = None):
    current_user = request.user
    event = events.objects.get(id=id)
    details = student_detail.objects.get(email=current_user)
    flag1=flag2=flag3=flag4=flag5=flag6=flag7=flag8=flag9=True
    if details.year == 'First':
        if event.registered11 >= event.quota11:
            flag1 = False
        if event.registered21 >= event.quota21:
            flag2 = False
        if event.registered31 >= event.quota31:
            flag3 = False
        if event.registered41 >= event.quota41:
            flag4 = False
        if event.registered51 >= event.quota51:
            flag5 = False
        if event.registered61 >= event.quota61:
            flag6 = False
        if event.registered71 >= event.quota71:
            flag7 = False
        if event.registered81 >= event.quota81:
            flag8 = False
        if event.registered91 >= event.quota91:
            flag9 = False
    elif details.year == 'Second':
        if event.registered12 >= event.quota12:
            flag1 = False
        if event.registered22 >= event.quota22:
            flag2 = False
        if event.registered32 >= event.quota32:
            flag3 = False
        if event.registered42 >= event.quota42:
            flag4 = False
        if event.registered52 >= event.quota52:
            flag5 = False
        if event.registered62 >= event.quota62:
            flag6 = False
        if event.registered72 >= event.quota72:
            flag7 = False
        if event.registered82 >= event.quota82:
            flag8 = False
        if event.registered92 >= event.quota92:
            flag9 = False
    elif details.year == 'Third':
        if event.registered13 >= event.quota13:
            flag1 = False
        if event.registered23 >= event.quota23:
            flag2 = False
        if event.registered33 >= event.quota33:
            flag3 = False
        if event.registered43 >= event.quota43:
            flag4 = False
        if event.registered53 >= event.quota53:
            flag5 = False
        if event.registered63 >= event.quota63:
            flag6 = False
        if event.registered73 >= event.quota73:
            flag7 = False
        if event.registered83 >= event.quota83:
            flag8 = False
        if event.registered93 >= event.quota93:
            flag9 = False
    try:
        network = follow_table.objects.get(current_user=current_user)
        network = network.connected_to.all()
        registered = event_registered_details.objects.filter(event=event)
        for obj in network:
            obj.flag = True
            for obj2 in registered:
                if obj == obj2.student:
                    obj.flag = False
    except follow_table.DoesNotExist:
        network = None
    if request.POST:
        code_id = str(event_registered_details.objects.filter(event=event).values('rcode').distinct().count()+1)
        if (len(code_id) == 1):
            rcode = event.prefix + '00' + code_id
        else:
            rcode = event.prefix + '0' + code_id
        if request.POST.get("marketing",False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.marketing = True
            regdetails.regmarketing = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=1)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size1-1):
                member = request.POST.get("mkt" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.marketing = True
                regdetails.regmarketing = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=1)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("finance", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.finance = True
            regdetails.regfinance = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=2)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size2-1):
                member = request.POST.get("fin" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.finance = True
                regdetails.regfinance = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=2)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("public_relations", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.public_relations = True
            regdetails.regpublic_relations = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=3)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size3-1):
                member = request.POST.get("pr" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.public_relations = True
                regdetails.regpublic_relations = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=3)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("human_resources", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.human_relations = True
            regdetails.reghuman_relations = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=4)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size4-1):
                member = request.POST.get("hr" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.human_relations = True
                regdetails.reghuman_relations = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=4)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("ent_dev", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.ent_dev = True
            regdetails.regent_dev = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=5)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size5-1):
                member = request.POST.get("ed" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.ent_dev = True
                regdetails.regent_dev = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=5)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("best_manager", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.best_manager = True
            regdetails.regbest_manager = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=6)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size6-1):
                member = request.POST.get("bm" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.best_manager = True
                regdetails.regbest_manager = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=6)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("corp_strg", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.corp_strg = True
            regdetails.regcorpstrg = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=7)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size7-1):
                member = request.POST.get("cs" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.corp_strg = True
                regdetails.regcorpstrg = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=7)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("quiz", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.quiz = True
            regdetails.regquiz = True
            # regdetails.team = True
            # regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=8)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size8-1):
                member = request.POST.get("qu" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.quiz = True
                regdetails.regquiz = True
                # regdetails.team = True
                # regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=8)
                # team.tcode = rcode
                # team.save()
        if request.POST.get("team", False):
            member = student.objects.get(email=current_user)
            event_registered.register(member, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
            regdetails.team = True
            regdetails.regteam = True
            regdetails.rcode = rcode
            regdetails.save()
            compute(regdetails.id, event.id)
            # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=9)
            # team.tcode = rcode
            # team.save()
            for x in range(0, event.team_size9-1):
                member = request.POST.get("te" + str(x))
                member = student.objects.get(email=member)
                event_registered.register(member, event)
                regdetails, created = event_registered_details.objects.get_or_create(event=event, student=member)
                regdetails.team = True
                regdetails.regteam = True
                regdetails.rcode = rcode
                regdetails.save()
                compute(regdetails.id, event.id)
                # team, created = teams.objects.get_or_create(event=event, club=club, student=member, type=9)
                # team.tcode = rcode
                # team.save()
        return HttpResponseRedirect("/user/student_dashboard/events")
    context = {'user':current_user,'event':event, "network":network, "flag1":flag1,"flag2":flag2,"flag3":flag3,
               "flag4":flag4,"flag5":flag5,"flag6":flag6,"flag7":flag7,"flag8":flag8,"flag9":flag9,
               'team1':range(0,event.team_size1-1),'team2':range(0,event.team_size2-1),
               'team3': range(0, event.team_size3-1), 'team4': range(0,event.team_size4-1),
               'team5': range(0, event.team_size5-1),'team6': range(0, event.team_size6-1),
               'team7': range(0, event.team_size7-1), 'team8': range(0, event.team_size8-1),
               'team9': range(0, event.team_size9-1),
            }
    if event.multiregistration:
        return render(request,'student_dash/register_details.html',context)
    else:
        return render(request, 'student_dash/solo_registration.html', context)


def upload_files(request,id):
    user = request.user
    round = rounds.objects.get(id = id)
    details = event_registered_details.objects.get(event=round.email,student=user)
    try:
        scores = round_scores.objects.get(student=user, round=round)
        scores = round_scores.objects.filter(rcode=scores.rcode, round=round)
    except round_scores.DoesNotExist:
        scores = round_scores(student=user, round=round, rcode=details.rcode)
    if request.POST:
        form = dataForm(request.POST, request.FILES)
        if form.is_valid():
            for score in scores:
                if form.cleaned_data.get("data1") != None:
                    score.data1 = form.cleaned_data.get("data1")
                if form.cleaned_data.get("data2") != None:
                    score.data2 = form.cleaned_data.get("data2")
                if form.cleaned_data.get("data3") != None:
                    score.data3 = form.cleaned_data.get("data3")
                score.rcode = details.rcode
                score.submitted = True
                deadline = score.round.deadline
                try:
                    score.submission_time = datetime.datetime.now()
                    if deadline < datetime.datetime.now():
                        score.late = True
                except:
                    score.late = False
                score.save()
            return HttpResponseRedirect("/user/student_dashboard")


def case_content(request,id):
    user =request.user
    round = rounds.objects.get(id=id)
    context = {'user':user, 'round':round}
    return render(request,'student_dash/case_content.html',context)


def review(request,id):
    user = request.user
    round = rounds.objects.get(id=id)
    scores = round_scores.objects.get(student=user,round=round)
    feasibility=creativity=communication=content=presentation=rebuttal=0
    if round.creativity:
        creativity = int((float(scores.creativity)/round.creativityvalue)*100)
        creativity = str(creativity)
    if round.communication:
        communication = int ((float(scores.communication)/round.communicationvalue)*100)
        communication = str(communication)
    if round.content:
        content = int((float(scores.content)/round.contentvalue)*100)
        content = str(content)
    if round.presentation:
        presentation = int ((float(scores.presentation)/round.presentationvalue)*100)
        presentation = str (presentation)
    if round.rebuttal:
        rebuttal = int ((float(scores.rebuttal)/round.rebuttalvalue)*100)
        rebuttal = str (rebuttal)
    if round.feasibility:
        feasibility = int ((float(scores.feasibility)/round.feasibilityvalue)*100)
        feasibility = str (feasibility)
    print(creativity)
    context = {'user':request.user,'scores':scores, 'round':round,'creativity':creativity,'communication':communication,'content':content,
               'presentation':presentation,'rebuttal':rebuttal,'feasibility':feasibility,}
    return render(request, 'student_dash/performance_review_new.html', context)


def edit_profile(request):
    user = request.user
    details = student_detail.objects.get(email=user)
    flag = 0
    if request.POST:
        user.name = request.POST.get("name")
        details.section = request.POST.get("section")
        user.phoneno = request.POST.get("phone")
        user.about = request.POST.get("about")
        if request.FILES['profile_pic']:
            user.profile_picture = request.FILES['profile_pic']
        if request.POST.get("old_password") != '' and request.POST.get("new_password") != '':
            old = request.POST.get("old_password")
            new = request.POST.get("new_password")
            if auth.authenticate(email=user.email, password=old):
                user.set_password(new)
                flag = 1
                user.save()
                details.save()
                auth.login(request, user)
            else:
                flag = 2
        user.save()
        details.save()
    context = {'user':user,'details':details,'flag':flag}
    return render(request,'student_dash/edit_profile.html',context)


def search(request):
    user = request.user
    college = student_detail.objects.get(email=user)
    college = college.college
    students = student_detail.objects.filter(college=college, email__club=False, email__judge=False,
                                             email__college=False)
    friends, created = follow_table.objects.get_or_create(current_user=user)
    friends = friends.connected_to.all()
    for stu in students:
        stu.flag = False
        for friend in friends:
            if stu.email == friend:
                stu.flag = True
    context = {'user': user, 'students': students}
    return render(request, 'student_dash/student_list.html', context)


def network(request):
    user = request.user
    college = student_detail.objects.get(email=user)
    college = college.college
    try:
        networks,created = follow_table.objects.get_or_create(current_user=user)
        networks = networks.connected_to.all()
    except:
        networks = None
    context = {'user': user,'students': networks}
    return render(request, 'student_dash/network.html', context)