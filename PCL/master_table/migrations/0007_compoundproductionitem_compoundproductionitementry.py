# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0006_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompoundProductionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType')),
            ],
        ),
        migrations.CreateModel(
            name='CompoundProductionItemEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_production_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.CompoundProductionItem')),
                ('production_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.ProductionItem')),
            ],
        ),
    ]
