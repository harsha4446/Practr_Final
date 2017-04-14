from django.conf.urls import url,include
from . import views
from profile_page.views import profile_page



urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
]
