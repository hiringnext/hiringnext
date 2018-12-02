# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-24 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0009_jobopening_default_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(blank=True, max_length=100, null=True)),
                ('question2', models.CharField(blank=True, max_length=100, null=True)),
                ('job_apply_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobopening.Jobopening')),
            ],
        ),
    ]