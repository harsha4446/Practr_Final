# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170324_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='club_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='colleges',
            name='college_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
