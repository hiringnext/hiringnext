# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_companyprofile_company_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='company_review',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Rate Company Out Of Five', max_digits=2, null=True),
        ),
    ]
