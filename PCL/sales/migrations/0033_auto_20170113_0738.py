# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0067_auto_20170106_1325'),
        ('sales', '0032_auto_20170113_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensedetail',
            name='deport',
        ),
        migrations.AddField(
            model_name='expensedetail',
            name='deport',
            field=models.ManyToManyField(to='master_table.Deport'),
        ),
        migrations.RemoveField(
            model_name='expensedetail',
            name='expense_criteria',
        ),
        migrations.AddField(
            model_name='expensedetail',
            name='expense_criteria',
            field=models.ManyToManyField(to='master_table.ExpenseCriteria', verbose_name='Expense Specification'),
        ),
    ]
