# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0017_auto_20181204_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='must_have_skills',
            field=models.TextField(blank=True, null=True, verbose_name='Must Have Skills'),
        ),
    ]