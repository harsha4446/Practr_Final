# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0060_auto_20170615_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='ext_judge',
            field=models.BooleanField(default=False),
        ),
    ]
