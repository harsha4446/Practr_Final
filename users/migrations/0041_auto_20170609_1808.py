# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20170609_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='college_name',
            field=models.CharField(choices=[('Christ University B.COM', 'Christ University B.COM'), ('Christ University D.M.S', 'Christ University D.M.S'), ('Christ University D.P.S', 'Christ University D.P.S'), ('Jain University SCS', 'Jain University SCS'), ('Jain University CMS', 'Jain University CMS'), ('Mount Carmel B.COM', 'Mount Carmel B.COM'), ('Mount Carmel BBA', 'Mount Carmel BBA'), ('St.Josephs B.COM', 'St.Josephs B.COM')], default='', max_length=200),
        ),
    ]