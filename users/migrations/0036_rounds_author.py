# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_judge_detail_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='author',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
