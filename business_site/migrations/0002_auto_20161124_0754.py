# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-24 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('business_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='website',
            name='publish',
        ),
        migrations.AddField(
            model_name='website',
            name='business',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websitecontrol',
            name='website',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business_site.Website'),
        ),
    ]
