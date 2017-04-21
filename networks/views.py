from django.shortcuts import render
from users.models import follow_table,student
from django.http import HttpResponseRedirect
# Create your views here.


def network(request):
    user = request.user
    friends = None
    try:
        friend = follow_table.objects.get(current_user=user)
        friends = friend.connected_to.all()
    except follow_table.DoesNotExist:
        friend = None
    context = {"user":user, "friends":friends,}
    return render(request,'networks/network.html',context)

def unfollow(request, id = None):
    if id != None:
        new_friend = student.objects.get(id = id)
        current_user = request.user
        follow_table.lose_friend(current_user,new_friend)
    return HttpResponseRedirect('/user/network/')