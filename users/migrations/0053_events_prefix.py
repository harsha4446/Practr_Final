# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_event_registered_details_rcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='prefix',
            field=models.CharField(default='', max_length=4),
        ),
    ]
