# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-05 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190405_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='Slug'),
        ),
    ]
