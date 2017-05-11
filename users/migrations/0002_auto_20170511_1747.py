# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge_detail',
            name='college',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='judge_detail',
            name='degree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='judge_detail',
            name='designation',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='judge_detail',
            name='industry_exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='judge_detail',
            name='round',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.rounds'),
        ),
        migrations.AddField(
            model_name='judge_detail',
            name='website',
            field=models.CharField(default='', max_length=500),
        ),
    ]
