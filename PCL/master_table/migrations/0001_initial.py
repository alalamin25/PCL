# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CompoundProductionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompoundProductionItemEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_amount', models.FloatField()),
                ('compound_production_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.CompoundProductionItem')),
            ],
        ),
        migrations.CreateModel(
            name='FinishedProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinishedProductItemLowerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinishedProductItemMiddleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundamentalProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RawItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('fundamental_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType')),
            ],
        ),
        migrations.CreateModel(
            name='RawItemLowerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('fundamental_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType')),
            ],
        ),
        migrations.CreateModel(
            name='RawItemMiddleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('fundamental_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone1', models.CharField(blank=True, max_length=30, null=True)),
                ('phone2', models.CharField(blank=True, max_length=30, null=True)),
                ('phone3', models.CharField(blank=True, max_length=30, null=True)),
                ('phone4', models.CharField(blank=True, max_length=30, null=True)),
                ('phone5', models.CharField(blank=True, max_length=30, null=True)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edit_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='rawitemlowercategory',
            name='middle_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.RawItemMiddleCategory'),
        ),
        migrations.AddField(
            model_name='rawitem',
            name='lower_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.RawItemLowerCategory'),
        ),
        migrations.AddField(
            model_name='rawitem',
            name='middle_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.RawItemMiddleCategory'),
        ),
        migrations.AddField(
            model_name='finishedproductitemmiddlecategory',
            name='fundamental_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType'),
        ),
        migrations.AddField(
            model_name='finishedproductitemlowercategory',
            name='fundamental_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType'),
        ),
        migrations.AddField(
            model_name='finishedproductitemlowercategory',
            name='middle_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FinishedProductItemMiddleCategory'),
        ),
        migrations.AddField(
            model_name='finishedproductitem',
            name='fundamental_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType'),
        ),
        migrations.AddField(
            model_name='finishedproductitem',
            name='lower_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FinishedProductItemLowerCategory'),
        ),
        migrations.AddField(
            model_name='finishedproductitem',
            name='middle_category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FinishedProductItemMiddleCategory'),
        ),
        migrations.AddField(
            model_name='compoundproductionitementry',
            name='production_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FinishedProductItem'),
        ),
        migrations.AddField(
            model_name='compoundproductionitem',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_table.FundamentalProductType'),
        ),
    ]
