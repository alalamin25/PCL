# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0056_deportoperation_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deportoperation',
            name='quantity',
            field=models.FloatField(default=1),
        ),
    ]
