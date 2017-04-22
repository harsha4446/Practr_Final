from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.dashboard,name='dash'),
    url(r'^clubs/$', views.clubs_view,name='clubs'),
    url(r'^register/(?P<id>\d+)/$', views.club_register, name='register'),
    url(r'^events/$', views.event_feed, name='events'),
    url(r'^search/$', views.search, name='seach'),

]