from django.conf.urls import url,include
from . import views


#yrls

urlpatterns = [
    url(r'^$', views.profile_page, name='profile_page'),
    url(r'^(?P<id>\d+)/$', views.profile_page, name='user_profile'),
    url(r'^connect/(?P<id>\d+)/$', views.connect, name='connect'),

]
