# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_remove_student_scores_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='weight',
            field=models.FloatField(default=1.0),
        ),
    ]
