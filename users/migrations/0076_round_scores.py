# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 23:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0075_auto_20170426_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='round_scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.IntegerField(default=0)),
                ('question2', models.IntegerField(blank=True, default=0, null=True)),
                ('question3', models.IntegerField(blank=True, default=0, null=True)),
                ('question4', models.IntegerField(blank=True, default=0, null=True)),
                ('question5', models.IntegerField(blank=True, default=0, null=True)),
                ('creativity', models.IntegerField(blank=True, default=0, null=True)),
                ('content', models.IntegerField(blank=True, default=0, null=True)),
                ('presentation', models.IntegerField(blank=True, default=0, null=True)),
                ('rebuttal', models.IntegerField(blank=True, default=0, null=True)),
                ('communication', models.IntegerField(blank=True, default=0, null=True)),
                ('feasibility', models.IntegerField(blank=True, default=0, null=True)),
                ('feedback', models.CharField(default='', max_length=1000)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_score', to='users.rounds')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]