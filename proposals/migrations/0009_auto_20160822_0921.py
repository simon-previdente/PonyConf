# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0008_auto_20160808_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ('event',)},
        ),
    ]
