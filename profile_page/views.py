from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import student_detail, judge_detail


# Create your views here.
def profile_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.user.judge:
        return HttpResponseRedirect('/user/judge_details')
    current_user = request.user
    user_details = student_detail.objects.get(email=current_user)
    context = {"user":current_user,"details":user_details,}
    return render(request,'profile_page/profile_page.html',context)