# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0051_auto_20170103_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='fplowercat',
            name='code',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
