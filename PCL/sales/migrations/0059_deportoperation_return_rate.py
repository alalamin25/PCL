# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0058_deportoperation_transection_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportoperation',
            name='return_rate',
            field=models.FloatField(default=0),
        ),
    ]
