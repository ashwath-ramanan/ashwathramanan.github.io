# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_animeseries_link1'),
    ]

    operations = [
        migrations.AddField(
            model_name='arcs',
            name='plink',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arcs',
            name='ylink',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
