# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-06 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_registerdstudents_place_comapany_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdstudents',
            name='place_comapany_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='addplace', to='teacher.AddPlacement'),
        ),
    ]
