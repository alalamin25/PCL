# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0063_delete_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.CharField(max_length=3, verbose_name='Supplier Code: ')),
                ('Customer_code', models.CharField(max_length=3, verbose_name='Customer Code: ')),
                ('bank_code', models.CharField(max_length=3, verbose_name='Customer Code: ')),
                ('deport_code', models.CharField(max_length=3, verbose_name='Customer Code: ')),
            ],
        ),
    ]
