# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0062_auto_20170122_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldetailinfo',
            name='product_code_text',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=''),
        ),
    ]
