from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^student_details/', include('profile_page.urls')),
    url(r'^personal_info', views.personal_info, name='personal_info'),
    url(r'^judge_details/', include('judge.urls')),
    url(r'^student_list/', include('studentlist.urls')),
]
