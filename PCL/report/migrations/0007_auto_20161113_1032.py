# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 10:32
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20161113_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finishedproductreport',
            name='middle_category_type',
            field=smart_selects.db_fields.ChainedManyToManyField(auto_choose=True, blank=True, chained_field='fundamental_type', chained_model_field='fundamental_type', to='master_table.FPMiddleCat'),
        ),
    ]
