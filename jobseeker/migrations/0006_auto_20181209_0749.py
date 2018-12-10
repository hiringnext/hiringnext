# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-09 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0005_auto_20181209_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='qualification',
            field=models.CharField(choices=[('PG', 'Post Graduate'), ('Graduate', 'Graduate'), ('UG', 'Under Graduate')], max_length=100),
        ),
        migrations.AlterField(
            model_name='refercandidate',
            name='qualification',
            field=models.CharField(choices=[('PG', 'Post Graduate'), ('Graduate', 'Graduate'), ('UG', 'Under Graduate')], max_length=100),
        ),
    ]
