# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_remove_arcs_ylink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arcs',
            name='plink',
            field=models.CharField(max_length=2000),
        ),
    ]
