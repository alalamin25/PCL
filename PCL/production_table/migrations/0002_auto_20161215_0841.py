# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production_table', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riissueentry',
            options={'verbose_name': 'Issued From Gowdown By Shifts', 'verbose_name_plural': 'Issued From Gowdown By Shifts'},
        ),
        migrations.AlterModelOptions(
            name='rireturnentry',
            options={'verbose_name': 'Returned To Gowdown', 'verbose_name_plural': 'Returned To Gowdown'},
        ),
    ]
