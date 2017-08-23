# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170813_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='college_name',
            field=models.CharField(choices=[('Christ University B.COM', 'Christ University B.COM'), ('Christ University D.M.S', 'Christ University D.M.S'), ('Christ University D.P.S', 'Christ University D.P.S'), ('Christ University, Bannerghatta', 'Christ University, Bannerghatta'), ('Presidency College', 'Presidency College'), ('Jain University SCS', 'Jain University SCS'), ('Jain University CMS', 'Jain University CMS'), ('Mount Carmel B.COM', 'Mount Carmel B.COM'), ('Mount Carmel BBA', 'Mount Carmel BBA'), ('St.Josephs B.COM', 'St.Josephs B.COM'), ('Kristu Jayanti College B.COM', 'Kristu Jayanti College  B.COM'), ('Kristu Jayanti College BBA', 'Kristu Jayanti College BBA'), ('KLE CBALC Belgaum', 'KLE CBALC Belgaum'), ('Bishop Cotton Womens College', 'Bishop Cotton Womens College'), ('Garden City College', 'Garden City College'), ('Trinity College of Commerce', 'Trinity College of Commerce'), ('Manipal University DOC', 'Manipal University DOC'), ('Vidhyaashram FGC', 'Vidhyaashram FGC')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='bmtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='cstotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='edtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='fintotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='hrtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='mkttotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='prtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='qutotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event_registered_details',
            name='tetotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='round_scores',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='degree',
            field=models.CharField(choices=[('B.COM', 'B.COM'), ('BBA', 'BBA'), ('BMS', 'BMS'), ('Other', 'Other')], default='', max_length=100),
        ),
    ]