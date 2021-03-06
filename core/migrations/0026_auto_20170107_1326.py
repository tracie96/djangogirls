# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20170107_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='applicants_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of applicants'),
        ),
        migrations.AddField(
            model_name='event',
            name='attendees_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of attendees'),
        ),
    ]
