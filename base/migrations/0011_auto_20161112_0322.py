# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 03:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0010_auto_20161111_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='email',
        ),
        migrations.AlterField(
            model_name='confirmemailorder',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 3, 22, 49, 274245)),
        ),
        migrations.AlterField(
            model_name='confirmemailorder',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 3, 22, 49, 274159)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2016, 11, 12, 3, 22, 49, 272304)),
        ),
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 12, 3, 22, 49, 272457)),
        ),
    ]
