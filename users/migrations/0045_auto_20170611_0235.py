# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20170609_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='quota11',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota12',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota13',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota21',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota22',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota23',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota31',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota32',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota33',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota41',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota42',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota43',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota51',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota52',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota53',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota61',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota62',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='quota63',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='about',
            field=models.CharField(default='', max_length=100),
        ),
    ]