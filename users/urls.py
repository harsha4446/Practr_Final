from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^student_details/', include('profile_page.urls')),
    url(r'^newstudent_info', views.new_student, name='newstudent'),
    url(r'^newjudge_info', views.new_judge, name='newjudge'),
    url(r'^newcollege_info', views.new_college, name='newcollege_info'),
    url(r'^newclub_info', views.new_club, name='newclub_info'),
    url(r'^judge_details/', include('judge.urls')),
    url(r'^club_dashboard/', include('club_dashboard.urls')),
    url(r'^college_dashboard/', include('college_dashboard.urls')),
    url(r'^student_dashboard/', include('student_dashboard.urls')),
    url(r'^judge_dashboard/', include('judge_dashboard.urls')),
    url(r'^network/', include('networks.urls')),
    url(r'^student/', views.registerStudent, name='student'),
    url(r'^club/', views.registerClub, name='club'),
    url(r'^university/', views.registerUni, name='uni'),
]
