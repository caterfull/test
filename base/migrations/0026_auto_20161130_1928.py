# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0025_auto_20161130_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stripesubscripcion',
            name='stripecustomer',
        ),
        migrations.DeleteModel(
            name='StripeSubscripcion',
        ),
    ]
