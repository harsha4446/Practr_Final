# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20170414_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow_table',
            name='asad',
        ),
        migrations.AddField(
            model_name='follow_table',
            name='connected_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow_table',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
