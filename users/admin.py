from django.contrib import admin
from .models import student,student_scores,colleges,clubs,interests, student_detail,judge_detail,events,rounds,follow_table
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
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