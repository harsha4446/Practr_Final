# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_round_scores_submission_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round_scores',
            name='submission_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
