# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20170530_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='multiregistration',
            field=models.BooleanField(default=True),
        ),
    ]