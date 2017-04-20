from django.conf.urls import url,include
from . import views
#try


urlpatterns = [
    url(r'^$', views.dashboard, name='judge_dash'),
]
