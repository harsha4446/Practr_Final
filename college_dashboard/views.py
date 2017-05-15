from django.shortcuts import render
from users.models import clubs,colleges
from django.http import HttpResponseRedirect
from users.forms import newClub
from users.models import student,clubs,colleges

# Create your views here.
def dashboard(request):
    user = request.user
    if not user.college:
        if user.club:
            return HttpResponseRedirect("/user/club_dashboard/")
        else:
            return HttpResponseRedirect("/user/student_dashboard/")
    college = colleges.objects.get(email = user)
    unverified_clubs = clubs.objects.filter(email = college, verified=False)
    context = {"user":user, "college":college, "unver_clubs":unverified_clubs}
    return render(request,'college_dash/dashboard.html',context)

def verified_clubs(request):
    user = request.user
    if not user.college:
        if user.club:
            return HttpResponseRedirect("/user/club_dashboard/")
        else:
            return HttpResponseRedirect("/user/student_dashboard/")
    college = colleges.objects.get(email=user)
    verified_clubs = clubs.objects.filter(email=college, verified=True)
    context = {"user": user, "college": college, "ver_clubs": verified_clubs}
    return render(request, 'college_dash/verified_clubs.html', context)

def add_club(request):
    user = request.user
    formClub = newClub(request.POST or None)
    college = colleges.objects.get(email = user)
    if formClub.is_valid():
        club = clubs(email = college)
        club.college = college.college_name
        club.verified = True
        club.name = formClub.cleaned_data.get("name")
        club.admin_name = formClub.cleaned_data.get("admin_name")
        club_password = formClub.cleaned_data.get("club_password")
        club.phone = formClub.cleaned_data.get("phone")
        club.club_email = formClub.cleaned_data.get("club_email")
        new_user = student.objects.create_user(club.club_email, club_password, club.admin_name, club.phone)
        new_user.club = True
        new_user.save()
        club.save()
        return HttpResponseRedirect('/user/college_dashboard/')
    context = {"form":formClub, }
    return render(request, 'college_dash/newclub.html', context)

def verify(request, id = None):
    club = clubs.objects.get(id = id)
    club.verified = True
    club.save()
    return HttpResponseRedirect('/user/college_dashboard/')