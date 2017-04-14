from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import student_detail, follow_table, student


# Create your views here.
def profile_page(request, id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.user.judge:
        return HttpResponseRedirect('/user/judge_details')
    if id is None:
        user = request.user
    else:
        user = student.objects.get(id = id)
    user_details = student_detail.objects.get(email=user)
    context = {"user":user,"details":user_details,}
    return render(request,'profile_page/profile_page.html',context)

def connect(request, id= None):
    if id != None:
        new_friend = student.objects.get(id = id)
        current_user = request.user
        follow_table.make_friend(current_user,new_friend)
    return HttpResponseRedirect('/profile_page/'+id)