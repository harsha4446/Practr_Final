from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.dashboard,name='clubdash'),

]