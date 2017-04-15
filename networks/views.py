from django.shortcuts import render
from users.models import follow_table,student
# Create your views here.


def network(request):
    user = request.user
    try:
        friend = follow_table.objects.get(current_user=user)
    except friend.DoesNotExist:
        friend = None
    friends = friend.connected_to.all()
    context = {"user":user, "friends":friends,}
    return render(request,'networks/network.html',context)
