from django.shortcuts import render
from users.models import event_registered, judge_detail, rounds, events, round_scores, student, clubs,event_registered_details,teams
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    user = request.user
    details = judge_detail.objects.get(email=user)
    event = events.objects.get(email=details.club, current=True)
    all_rounds = rounds.objects.filter(email=event, type=details.type)
    register = 0
    corename = None
    if details.type == 1:
        corename = 'Marketing'
    elif details.type == 2:
        corename = 'Finance'
    elif details.type == 3:
        corename = 'Public Relations'
    elif details.type == 4:
        corename = 'Human Resource'
    elif details.type == 5:
        corename = 'Entrepreneurship Development'
    elif details.type == 6:
        corename = 'Best Manager'
    elif details.type == 7:
        corename = 'Corperate Strategy'
    elif details.type == 8:
        corename = 'Quiz'
    elif details.type == 9:
        corename = 'Team'
    context = {'all_rounds': all_rounds, 'user': request.user, 'event': event, 'type': details.type, 'count': register,
               'corename':corename}
    return render(request, 'club_dash/case_view.html', context)


def judge_view(request,id):
    user = request.user
    round = rounds.objects.get(id=id)
    registered = None
    try:
        if not round.email.inter_type:
            #registered = round_scores.objects.filter(round=round,submitted=True)
            registered = round_scores.objects.filter(round=round)
        else:
            #registered = round_scores.objects.filter(round=round)
            all_registered = round_scores.objects.filter(round=round).order_by('rcode')
            rcode = None
            print(all_registered)
            for member in all_registered:
                if rcode != member.rcode:
                    rcode = member.rcode
                    print(member)
                    if registered == None:
                        registered = round_scores.objects.filter(round=round,student=member.student)
                    else:
                        registered = registered | round_scores.objects.filter(round=round,student=member.student)
                    print(registered)
    except event_registered.DoesNotExist:
        registered = None
    context = {'user': user, 'registered': registered, 'round': round}
    return render(request, 'judge_dash/dashboard.html', context)


def assessment(request,pk=None,id=None):
    user = request.user
    round = rounds.objects.get(id=id)
    scores = None
    total = None
    form = None
    if pk != '0':
        judging = student.objects.get(id=pk)
        form = round_scores.objects.get(student=judging,round=round)
        scores = round_scores.objects.filter(round=round, rcode=form.rcode)
        # team = teams.objects.get(student=judging,event=round.email,type=round.type)
        # team = teams.objects.filter(cl)
    if request.POST:
        for score in scores:
            if score.judged == False:
                score.question1 = request.POST.get("question1"+pk,0)
                score.question2 = request.POST.get("question2"+pk,0)
                score.question3 = request.POST.get("question3"+pk,0)
                score.question4 = request.POST.get("question4"+pk,0)
                score.question5 = request.POST.get("question5"+pk,0)
                score.creativity = request.POST.get("creativity1"+pk,0)
                score.communication = request.POST.get("communication1"+pk,0)
                score.content = request.POST.get("content1"+pk,0)
                score.feasibility = request.POST.get("feasibility1"+pk,0)
                score.rebuttal = request.POST.get("rebuttal1"+pk,0)
                score.presentation = request.POST.get("presentation1"+pk,0)
                score.feedback = request.POST.get("feedback"+pk,'')
                score.judged_value = score.judged_value + 1
            else:
                score.question1 = score.question1 * score.judged_value
                score.question2 = score.question2 * score.judged_value
                score.question3 = score.question3 * score.judged_value
                score.question4 = score.question4 * score.judged_value
                score.question5 = score.question5 * score.judged_value
                score.creativity = score.creativity * score.judged_value
                score.communication = score.communication * score.judged_value
                score.feasibility = score.feasibility * score.judged_value
                score.rebuttal = score.rebuttal * score.judged_value
                score.presentation = score.presentation * score.judged_value
                score.content = score.content * score.judged_value
                score.judged_value = score.judged_value + 1
                score.question1 = float((score.question1 + float (request.POST.get("question1"+pk, 0)))/float(score.judged_value))
                score.question2 = float((score.question2 + float (request.POST.get("question2"+pk, 0)))/float(score.judged_value))
                score.question3 = float((score.question3 + float (request.POST.get("question3"+pk, 0)))/float(score.judged_value))
                score.question4 = float((score.question4 + float (request.POST.get("question4"+pk, 0)))/float(score.judged_value))
                score.question5 = float((score.question5 + float (request.POST.get("question5"+pk, 0)))/float(score.judged_value))
                score.creativity = float((score.creativity + float (request.POST.get("creativity1"+pk, 0)))/float(score.judged_value))
                score.communication = float((score.communication + float (request.POST.get("communication1"+pk, 0)))/float(score.judged_value))
                score.content = float((score.content + float (request.POST.get("content1"+pk, 0)))/float(2))
                score.feasibility = float((score.feasibility + float (request.POST.get("feasibility1"+pk, 0)))/float(2))
                score.rebuttal = float((score.rebuttal + float (request.POST.get("rebuttal1"+pk, 0)))/float(2))
                score.presentation = float((score.presentation + float (request.POST.get("presentation1"+pk, 0)))/float(2))
                if request.POST.get("feedback"+pk) != '':
                    if score.feedback == 'No Feedback Available':
                        score.feedback = request.POST.get("feedback"+pk, '')
                    else:
                        score.feedback = score.feedback + '<br>' + request.POST.get("feedback"+pk, '')
            score.total = float(float(score.question1)+float(score.question2)+float(score.question3)+float(score.question4)+float(score.question5)+float(score.creativity)+float(score.feasibility)+float(score.content)+float(score.communication)+float(score.rebuttal)+float(score.presentation))
            #score.total = int (float(round.weight)*score.total)
            score.judged = True
            score.save()
        return HttpResponseRedirect("/user/judge_dashboard/judge_view/"+id)
    context = {'user':user,'round':round,'scores':form}
    return render(request,'judge_dash/assessment_form.html',context)