# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production_table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionentry',
            old_name='raw_item',
            new_name='production_item',
        ),
    ]
