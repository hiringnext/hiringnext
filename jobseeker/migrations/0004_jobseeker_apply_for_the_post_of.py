# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0004_auto_20181101_1801'),
        ('jobseeker', '0003_auto_20181101_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='apply_for_the_post_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobopening.Jobopening'),
        ),
    ]