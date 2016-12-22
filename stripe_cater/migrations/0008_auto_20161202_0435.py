# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stripe_cater', '0007_auto_20161202_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='description',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge',
            name='stripe_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
