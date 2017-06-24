from django.shortcuts import render
from users.models import colleges,student_detail, events, follow_table, clubs, register_table, rounds, event_registered,student, round_scores,judge_detail, event_registered_details
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .forms import dataForm,detailFrom
from django.contrib import auth

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
    try:
         register = event_registered.objects.get(current_user = current_user)
         registered = register.registered_to.all()
         for x in registered:
             detail = event_registered_details.objects.get(student=current_user, event=x)
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
             if all_rounds is None:
                 all_rounds = round
             else:
                 all_rounds = all_rounds | round
    except event_registered.DoesNotExist:
        registered = None
        return render(request, 'student_dash/noEvent.html', {'user': current_user})
    except rounds.DoesNotExist:
        round = None
    context = {"rounds":all_rounds, "user":current_user, "form":form,'registered':registered }
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
        all_events = events.objects.filter(current=True, registration=True, email__college=details.college)
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
    flag1=flag2=flag3=flag4=flag5=flag6=True
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
    try:
        network = follow_table.objects.get(current_user=current_user)
        network = network.connected_to.all()
    except follow_table.DoesNotExist:
        network = None
    if request.POST:
        if event.multiregistration:
            event_registered.register(current_user, event)
            regdetails , created = event_registered_details.objects.get_or_create(event=event, student=current_user)
            regdetails.human_resources = request.POST.get("human_resources", False)
            regdetails.marketing = request.POST.get("marketing", False)
            regdetails.finance = request.POST.get("finance", False)
            regdetails.public_relations = request.POST.get("public_relations", False)
            regdetails.best_manager = request.POST.get("best_manager", False)
            regdetails.ent_dev = request.POST.get("ent_dev", False)
            if regdetails.rcode == '':
                code_id = str(event_registered_details.objects.filter(event=event).count())
                if (len(code_id) == 1):
                    regdetails.rcode = event.prefix + '00' + code_id
                if (len(code_id) == 2):
                    regdetails.rcode = event.prefix + '0' + code_id
            regdetails.save()
            compute(regdetails.id, event.id)
            return HttpResponseRedirect("/user/student_dashboard/events")
        else:
            event_registered.register(current_user, event)
            regdetails, created = event_registered_details.objects.get_or_create(event=event, student=current_user)
            regdetails.marketing = request.POST.get("marketing",False)
            regdetails.human_resources = request.POST.get("human_resources",False)
            regdetails.finance = request.POST.get("finance",False)
            regdetails.public_relations = request.POST.get("public_relations",False)
            regdetails.best_manager = request.POST.get("best_manager",False)
            regdetails.ent_dev = request.POST.get("ent_dev",False)
            if regdetails.rcode == '':
                code_id = str(event_registered_details.objects.filter(event=event).count())
                if (len(code_id) == 1):
                    regdetails.rcode = event.prefix + '00' + code_id
                if (len(code_id) == 2):
                    regdetails.rcode = event.prefix + '0' + code_id
            regdetails.save()
            compute(regdetails.id, event.id)
            return HttpResponseRedirect("/user/student_dashboard/events")
    context = {'event':event, "network":network, "flag1":flag1,"flag2":flag2,"flag3":flag3,
               "flag4":flag4,"flag5":flag5,"flag6":flag6}
    if event.multiregistration:
        return render(request,'student_dash/register_details.html',context)
    else:
        return render(request, 'student_dash/solo_registration.html', context)


def search(request):
    all_users = student.objects.filter(judge=False, college=False, club=False)
    context = {"all_users": all_users, }
    return render(request, 'student_dash/student_list.html', context)


def upload_files(request,id):
    user = request.user
    round = rounds.objects.get(id = id)
    details = event_registered_details.objects.get(event=round.email,student=user)
    try:
        scores = round_scores.objects.get(student=user, round=round)
    except round_scores.DoesNotExist:
        scores = round_scores(student=user, round=round, rcode=details.rcode)
    if request.POST:
        form = dataForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get("data1") != None:
                scores.data1 = form.cleaned_data.get("data1")
            if form.cleaned_data.get("data2") != None:
                scores.data2 = form.cleaned_data.get("data2")
            if form.cleaned_data.get("data3") != None:
                scores.data3 = form.cleaned_data.get("data3")
            scores.rcode = details.rcode
            scores.submitted = True
            scores.save()
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
        creativity = int((scores.creativity/round.creativityvalue)*100)
        creativity = str(creativity)
        print("here")
    if round.communication:
        communication = int ((scores.communication/round.communicationvalue)*100)
        communication = str(communication)
    if round.content:
        content = int((scores.content/round.contentvalue)*100)
        content = str(content)
    if round.presentation:
        presentation = int ((scores.presentation/round.presentationvalue)*100)
        presentation = str (presentation)
    if round.rebuttal:
        rebuttal = int ((scores.rebuttal/round.rebuttalvalue)*100)
        rebuttal = str (rebuttal)
    if round.feasibility:
        feasibility = int ((scores.feasibility/round.feasibilityvalue)*100)
        feasibility = str (feasibility)
    print(creativity)
    context = {'user':request.user,'scores':scores, 'round':round,'creativity':creativity,'communication':communication,'content':content,
               'presentation':presentation,'rebuttal':rebuttal,'feasibility':feasibility,}
    return render(request,'student_dash/performance_review.html',context)


def edit_profile(request):
    user = request.user
    details = student_detail.objects.get(email=user)
    flag = 0
    if request.POST:
        user.name = request.POST.get("name")
        details.section = request.POST.get("section")
        user.phoneno = request.POST.get("phone")
        user.about = request.POST.get("about")
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