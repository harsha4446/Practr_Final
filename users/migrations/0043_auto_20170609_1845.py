# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20170609_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='degree',
            field=models.CharField(choices=[('B.COM', 'B.COM'), ('BBA', 'BBA')], default='', max_length=100),
        ),
    ]
