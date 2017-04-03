from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import judge_detail
# Create your views here.


#delete later

def judge_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if not request.user.judge:
        return HttpResponseRedirect('/user/student_details')
    user = request.user
    details = judge_detail.objects.get(email=user.email)
    context = {'user':user, "details":details,}
    return render(request,'judge/judge_page.html',context)
