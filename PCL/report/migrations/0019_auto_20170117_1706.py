# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0018_auto_20170117_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='fundamental_type_chained',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_chained', to='master_table.FundamentalProductType', verbose_name='Fundamental Type'),
        ),
    ]
