# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20170626_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round_scores',
            name='data1',
            field=models.FileField(blank=True, null=True, upload_to=users.models.round_data),
        ),
        migrations.AlterField(
            model_name='round_scores',
            name='data2',
            field=models.FileField(blank=True, null=True, upload_to=users.models.round_data),
        ),
        migrations.AlterField(
            model_name='round_scores',
            name='data3',
            field=models.FileField(blank=True, null=True, upload_to=users.models.round_data),
        ),
    ]
