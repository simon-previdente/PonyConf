# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0024_auto_20161024_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='label',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Label on program'),
        ),
    ]