# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-20 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20170519_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='qualified',
            field=models.IntegerField(default=2),
        ),
    ]
