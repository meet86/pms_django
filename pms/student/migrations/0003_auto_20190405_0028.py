# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190404_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdstudents',
            old_name='registered_student_name',
            new_name='registered_student_id',
        ),
    ]