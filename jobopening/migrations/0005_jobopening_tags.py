# Generated by Django 2.1.3 on 2018-11-10 03:31

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('jobopening', '0004_auto_20181101_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopening',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
