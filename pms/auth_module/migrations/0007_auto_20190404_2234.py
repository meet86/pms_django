# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0006_user_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
