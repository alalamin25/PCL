# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0072_auto_20170221_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deportoperation',
            name='return_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
