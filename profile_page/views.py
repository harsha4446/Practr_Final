from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import student_detail, follow_table, student, student_scores, clubs


def getmin(score):
    if score <= 80:
        return 0
    if score <= 200:
        return 81
    if score <= 350:
        return 201
    if score <= 550:
        return 351
    if score <= 800:
        return 551

def getmax(score):
    if score <= 80:
        return 80
    if score <= 200:
        return 200
    if score <= 350:
        return 350
    if score <= 550:
        return 550
    if score <= 800:
        return 800

def getlevel(score):
    if score <= 80:
        return 1
    if score <= 200:
        return 2
    if score <= 350:
        return 3
    if score <= 550:
        return 4
    if score <= 800:
        return 5


def studentprofile(request, id=None):
    user = student.objects.get(id=id)
    try:
        scores = student_scores.objects.get(username=user)
        creativitymax = getmax(scores.creativity)
        presentationmax = getmax(scores.presentation)
        rebuttalmax = getmax(scores.rebuttal)
        communicationmax = getmax(scores.communication)
        contentmax = getmax(scores.content)
        feasibilitymax = getmax(scores.feasibility)
        creativitylevel = getlevel(creativitymax)
        presentationlevel = getlevel(presentationmax)
        rebuttallevel = getlevel(rebuttalmax)
        communicationlevel = getlevel(communicationmax)
        contentlevel = getlevel(contentmax)
        feasibilitylevel = getlevel(feasibilitymax)
        creativitypercent = int ((scores.creativity/creativitymax)*100)
        feasibilitypercent = int((scores.feasibility / feasibilitymax) * 100)
        presentationpercent = int((scores.presentation / presentationmax) * 100)
        rebuttalpercent = int((scores.rebuttal / rebuttalmax) * 100)
        communicationpercent = int((scores.communication / communicationmax) * 100)
        contentpercent = int((scores.content / contentmax) * 100)
        user_details = student_detail.objects.get(email=user)
        context = {"user": user, "details": user_details,
               'creativitymax': creativitymax, 'presentationmax': presentationmax, 'rebuttalmax': rebuttalmax,
               'communicationmax': communicationmax,
               'contentmax': contentmax, 'feasibilitymax': feasibilitymax, 'creativitylevel': creativitylevel,
               'presentationlevel': presentationlevel,
               'rebuttallevel': rebuttallevel, 'communicationlevel': communicationlevel, 'contentlevel': contentlevel,
               'feasibilitylevel': feasibilitylevel,
               'score': scores,'creativitypercent':creativitypercent,'feasibilitypercent':feasibilitypercent,
                  'presentationpercent':presentationpercent,'rebuttalpercent':rebuttalpercent,
                   'communicationpercent':communicationpercent,'contentpercent':contentpercent}
        return context
    except student_scores.DoesNotExist:
        context = {}
        return context

def profile_page(request, id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.user.judge:
        return HttpResponseRedirect('/user/judge_details')
    else:
        context = studentprofile(request,id)
        return render(request, 'profile_page/profile_page.html', context)

def profile_club(request,id=None):
    club = clubs.objects.get(id=id)
    user = student.objects.get(email=club.club_email)
    context = {'user': user, 'club': club}
    return render(request, 'profile_page/club_profile.html', context)

def connect(request, id= None):
    if id != None:
        new_friend = student.objects.get(id = id)
        current_user = request.user
        follow_table.make_friend(current_user,new_friend)
    return HttpResponseRedirect('/profile_page/'+id)