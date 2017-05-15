from django.conf.urls import url,include
from . import views
#try


urlpatterns = [
    url(r'^$', views.dashboard, name='judge_dash'),
    url(r'^judge/(?P<pk>\d+)/$', views.assessment, name='assessment'),
]
