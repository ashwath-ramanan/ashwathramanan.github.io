# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_remove_animeseries_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arcs',
            name='ylink',
        ),
    ]
