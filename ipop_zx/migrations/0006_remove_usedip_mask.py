# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0005_auto_20180405_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usedip',
            name='mask',
        ),
    ]
