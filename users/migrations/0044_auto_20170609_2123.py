# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20170609_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='firstyear',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='events',
            name='secondyear',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='events',
            name='thirdyear',
            field=models.BooleanField(default=True),
        ),
    ]
