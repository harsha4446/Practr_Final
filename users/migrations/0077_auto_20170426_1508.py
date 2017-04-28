# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0076_round_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='round_scores',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='round_scores',
            name='question1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
