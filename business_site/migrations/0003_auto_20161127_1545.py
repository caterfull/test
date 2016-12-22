# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('business_site', '0002_auto_20161124_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='description',
        ),
        migrations.RemoveField(
            model_name='links',
            name='link',
        ),
        migrations.AddField(
            model_name='links',
            name='facebookpage',
            field=models.URLField(default='twitter.com'),
        ),
        migrations.AddField(
            model_name='links',
            name='instagram',
            field=models.URLField(default='twitter.com'),
        ),
        migrations.AddField(
            model_name='links',
            name='twitter',
            field=models.URLField(default='twitter.com'),
        ),
        migrations.AlterField(
            model_name='website',
            name='business',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.Business'),
        ),
    ]