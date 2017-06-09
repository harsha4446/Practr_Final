from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.dashboard,name='clubdash'),
    url(r'^live/(?P<id>\d+)/$', views.activate,name='openRegistration'),
    url(r'^new_event/(?P<access>\d+)/$$', views.add_event,name='newEvent'),
    url(r'^addRound/(?P<id>\d+)/(?P<operation>\d+)/(?P<offline>\d+)/$', views.add_round,name='newRound'),
    url(r'^delEvent/(?P<id>\d+)/$', views.del_event,name='delEvent'),
    #url(r'^subEvents/(?P<id>\d+)/$', views.sub_events,name='subevent'),
    url(r'^caseView/(?P<id>\d+)/(?P<type>\d+)/$', views.case_view,name='caseview'),
    url(r'^publish/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.publish,name='publish'),
    url(r'^members/(?P<id>\d+)/(?P<type>\d+)/$', views.members, name='members'),
    url(r'^result/(?P<round>\d+)/$', views.result, name='result'),
    url(r'^addRoom/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.addRoom, name='addRoom'),
    url(r'^addJudge/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.addJudge, name='addJudge'),
    url(r'^teamSize/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.teamSize, name='team'),
    url(r'^audience/(?P<id>\d+)/(?P<event>\d+)/(?P<type>\d+)/$', views.audience, name='audience'),
    url(r'^addSub/(?P<id>\d+)/(?P<type>\d+)/$', views.addSub, name='addSub'),
    url(r'^quotaset/(?P<id>\d+)$', views.quotaset, name='quota'),
]