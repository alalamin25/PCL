# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0057_auto_20170105_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fplowercat',
            name='code',
            field=models.CharField(max_length=1, unique=True),
        ),
    ]
