# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_round_scores_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='communicationvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rounds',
            name='contentvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rounds',
            name='creativityvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rounds',
            name='feasibilityvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rounds',
            name='presentationvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rounds',
            name='rebuttalvalue',
            field=models.IntegerField(default=0),
        ),
    ]