# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_auto_20170611_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interests',
            old_name='business_quiz',
            new_name='best_manager',
        ),
    ]