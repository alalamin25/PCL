# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0019_payment_deport_code_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='deport_code_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
    ]
