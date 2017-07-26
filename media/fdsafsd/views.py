from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import inform
from django.contrib import auth
# Create your views here.

def lock(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    user = request.user
    username = request.user.email
    auth.logout(request)
    form = inform(request.POST or None)
    if form.is_valid():
        password = inform.cleaned_data['password']
        user = auth.authenticate(email = username,password = password)
        auth.login(request,user)
        return HttpResponseRedirect("/user/student_dashboard/")
    context =  {'user':user, 'form':form}
    return render(request,'lock_screen/lock_screen.html',context)