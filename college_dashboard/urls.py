from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.dashboard,name='dash'),
    url(r'^new_club/$', views.add_club,name='newclub'),
]
