# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0052_fplowercat_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpmiddlecat',
            name='code',
            field=models.CharField(max_length=1, unique=True),
        ),
    ]
