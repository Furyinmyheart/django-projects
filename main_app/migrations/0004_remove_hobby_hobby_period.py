# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_study_study_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby',
            name='hobby_period',
        ),
    ]
