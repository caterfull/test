# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-03 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('stripe_cater', '0010_auto_20161203_1734'),
        ('base', '0026_auto_20161130_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='accout_creation_token',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='stripe_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='stripe_cater.StripeAccount'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='stripe_cater.PaymentOrder'),
        ),
    ]
