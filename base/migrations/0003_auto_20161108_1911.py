# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 19:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0002_auto_20161108_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.N_Company'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefix',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='suffix',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2016, 11, 8, 19, 11, 58, 365258)),
        ),
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 8, 19, 11, 58, 365297)),
        ),
    ]
