# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0055_auto_20170105_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='rimiddlecat',
            name='code',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
