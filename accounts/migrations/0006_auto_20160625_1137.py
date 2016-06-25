# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_participation_sound'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 11, 37, 1, 575397, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participation',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 25, 11, 37, 5, 56658, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 11, 37, 6, 538667, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 25, 11, 37, 7, 804703, tzinfo=utc)),
            preserve_default=False,
        ),
    ]