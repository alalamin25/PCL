# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_table', '0006_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_amount', models.FloatField()),
                ('invoice_no', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edit_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('raw_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.ProductionItem')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.Shift')),
            ],
        ),
    ]
