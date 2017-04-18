from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.dashboard,name='clubdash'),
    url(r'^(?P<id>\d+)/$', views.activate,name='openRegistration'),
    url(r'^new_event/$', views.add_event,name='newEvent'),
    url(r'^addRound/(?P<id>\d+)/$', views.add_round,name='newRound'),
    url(r'^delEvent/(?P<id>\d+)/$', views.del_event,name='delEvent'),

]