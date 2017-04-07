from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^student_details/', include('profile_page.urls')),
    url(r'^newstudent_info', views.new_student, name='newstudent'),
    url(r'^newjudge_info', views.new_judge, name='newjudge'),
    url(r'^newcollege_info', views.new_college, name='newcollege_info'),
    url(r'^judge_details/', include('judge.urls')),
    url(r'^student_list/', include('studentlist.urls')),
    url(r'^club_dashboard/', include('club_dashboard.urls')),
]
