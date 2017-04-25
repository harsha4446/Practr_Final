from django.shortcuts import render
from users.models import event_registered

# Create your views here.
def dashboard(request):
    user = request.user
    context = {'user':user,}
    try:
        event = event_registered.objects.get(current_user = user)
        events = event.registered_to.all()
    except event_registered.DoesNotExist:
        events = None
    context ={'user':user, 'events':events}
    return render(request,'',context)