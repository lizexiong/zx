# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0008_auto_20180405_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedip',
            name='mask',
            field=models.CharField(default='255.255.255.0', max_length=16),
        ),
    ]
