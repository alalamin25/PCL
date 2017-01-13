# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0067_auto_20170106_1325'),
        ('report', '0004_auto_20170113_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='customer',
            field=models.ManyToManyField(blank=True, null=True, to='master_table.Customer'),
        ),
    ]
