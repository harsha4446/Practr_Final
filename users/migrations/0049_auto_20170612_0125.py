# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_registered_details',
            name='teammate1',
        ),
        migrations.RemoveField(
            model_name='event_registered_details',
            name='teammate2',
        ),
        migrations.RemoveField(
            model_name='event_registered_details',
            name='teammate3',
        ),
        migrations.AddField(
            model_name='rounds',
            name='resource1data',
            field=models.FileField(null=True, upload_to=users.models.round_data),
        ),
        migrations.AddField(
            model_name='rounds',
            name='resource2data',
            field=models.FileField(null=True, upload_to=users.models.round_data),
        ),
        migrations.AddField(
            model_name='rounds',
            name='resource3data',
            field=models.FileField(null=True, upload_to=users.models.round_data),
        ),
        migrations.AddField(
            model_name='rounds',
            name='resource4data',
            field=models.FileField(null=True, upload_to=users.models.round_data),
        ),
        migrations.AddField(
            model_name='rounds',
            name='resource5data',
            field=models.FileField(null=True, upload_to=users.models.round_data),
        ),
    ]
