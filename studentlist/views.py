from django.shortcuts import render
from users.models import student
from . forms import userForm

# Create your views here.

def student_list(request):
    all_users = student.objects.filter(judge=False)
    formuser = userForm(request.POST or None)

    if formuser.is_valid() and formuser.cleaned_data['email'] != '':
        email = formuser.cleaned_data['email']
        all_users = student.objects.filter(judge=False,email=email)

    if formuser.is_valid()and formuser.cleaned_data['name'] != '':
        name = formuser.cleaned_data['name']
        all_users = student.objects.filter(judge=False,name=name)

    if formuser.is_valid()and formuser.cleaned_data['college'] != '':
        college = formuser.cleaned_data['college']
        all_users = student.objects.filter(judge=False,student_detail__college=college)

    context = {"all_users":all_users,"form":formuser,}
    return render (request,'student_list/student_list.html',context)