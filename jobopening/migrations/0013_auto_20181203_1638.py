# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0012_auto_20181203_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='max_salary_budget',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Max. Salary Criteria'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='min_salary_budget',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Min. Salary Criteria'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='referral_reward',
            field=models.DecimalField(decimal_places=0, max_digits=5, null=True, verbose_name='Referral Amount'),
        ),
    ]