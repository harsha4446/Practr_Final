# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170519_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core1',
            new_name='best_manager',
        ),
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core2',
            new_name='ent_dev',
        ),
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core3',
            new_name='finance',
        ),
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core4',
            new_name='human_resources',
        ),
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core5',
            new_name='marketing',
        ),
        migrations.RenameField(
            model_name='event_registered_details',
            old_name='core6',
            new_name='public_relations',
        ),
    ]
