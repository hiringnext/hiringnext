# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0002_auto_20181101_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignstaff',
            name='assign_recruiter_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
