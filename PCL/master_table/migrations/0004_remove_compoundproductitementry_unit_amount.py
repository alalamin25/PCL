# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0003_remove_compoundproductitem_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compoundproductitementry',
            name='unit_amount',
        ),
    ]
