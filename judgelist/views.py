from django.shortcuts import render
from users.models import student,judge_detail
from studentlist.forms import userForm

# Create your views here.
def judge_list(request):
     all_users = student.objects.filter(judge=True)
     search = userForm(request.POST or None)

     if search.is_valid() and search.cleaned_data['email'] != '':
        email = search.cleaned_data['email']
        all_users = student.objects.filter(judge=True, email=email)

     if search.is_valid() and search.cleaned_data['name'] != '':
        name = search.cleaned_data['name']
        all_users = student.objects.filter(judge=True, name=name)

     if search.is_valid() and search.cleaned_data['interest'] != '':
        interested = search.cleaned_data['interest']
        users = student.objects.filter(judge=True)
        all_users = judge_detail.objects.filter(email=users, interested=True)

     context = {"all_users": all_users, "search":search, }
     return render(request, 'judge_list/judge_list.html', context)
