# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160509_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptimes',
            name='stop_headsign',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
