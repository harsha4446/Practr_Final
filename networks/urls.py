from django.conf.urls import url,include
from . import views



urlpatterns = [
    url(r'^$', views.network, name='network'),
    url(r'^unfollow/(?P<id>\d+)/(?P<flag>\d+)/$', views.unfollow, name='unfollow'),
]
