from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.dashboard,name='dash'),
    url(r'^clubs/$', views.clubs_view,name='clubs'),
    url(r'^register/(?P<id>\d+)/$', views.club_register, name='club_register'),
    url(r'^events/$', views.event_feed, name='events'),
    url(r'^search/$', views.search, name='seach'),
    url(r'^eventRegister/(?P<id>\d+)/$', views.event_register, name='event_register'),
    url(r'^upload_files/(?P<id>\d+)/$', views.upload_files, name='upload'),
    url(r'^case_content/(?P<id>\d+)/$', views.case_content, name='context'),
    url(r'^review/$', views.review, name='review'),

]