from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.dashboard,name='clubdash'),
    url(r'^(?P<id>\d+)/$', views.activate,name='openRegistration'),
    url(r'^new_event/$', views.add_event,name='newEvent'),
    url(r'^addRound/(?P<id>\d+)/(?P<operation>\d+)/$', views.add_round,name='newRound'),
    url(r'^delEvent/(?P<id>\d+)/$', views.del_event,name='delEvent'),
    url(r'^subEvents/(?P<id>\d+)/$', views.sub_events,name='subevent'),
    url(r'^caseView/(?P<id>\d+)/(?P<type>\d+)/$', views.case_view,name='caseview'),
    url(r'^publish/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.publish,name='publish'),
    url(r'^members/$', views.members, name='members'),


]