# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0062_auto_20170106_1242'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code',
        ),
    ]
