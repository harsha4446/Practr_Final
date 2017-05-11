from django.contrib import admin
from .models import student,student_scores,colleges,clubs,interests, student_detail,judge_detail,\
    events,rounds,follow_table, register_table, event_registered, round_room, room_judge, round_scores
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)
admin.site.register(student)
admin.site.register(student_scores)
admin.site.register(colleges)
admin.site.register(clubs)
admin.site.register(interests)
admin.site.register(student_detail)
admin.site.register(judge_detail)
admin.site.register(events)
admin.site.register(rounds)
admin.site.register(follow_table)
admin.site.register(register_table)
admin.site.register(event_registered)
admin.site.register(round_room)
admin.site.register(room_judge)
admin.site.register(round_scores)