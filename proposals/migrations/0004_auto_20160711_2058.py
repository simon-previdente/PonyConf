# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20160711_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together=set([('site', 'name')]),
        ),
    ]