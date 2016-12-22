# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-03 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stripe_cater', '0009_auto_20161202_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_publishable_key', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=50)),
                ('stripe_user_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='charge',
            name='currency',
            field=models.CharField(default='usd', max_length=3),
        ),
        migrations.AddField(
            model_name='charge',
            name='source',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
