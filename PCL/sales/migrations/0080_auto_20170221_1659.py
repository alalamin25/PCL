# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0079_auto_20170221_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='deport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.Deport', to_field='code', verbose_name='Depot'),
        ),
    ]
