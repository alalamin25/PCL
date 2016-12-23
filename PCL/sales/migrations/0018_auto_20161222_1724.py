# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0017_auto_20161222_1035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Credit',
            new_name='Payment',
        ),
        migrations.AlterField(
            model_name='deportoperation',
            name='fundamental_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType'),
        ),
    ]
