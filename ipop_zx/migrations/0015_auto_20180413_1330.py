# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0014_auto_20180407_2338'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usedip',
            unique_together=set([('network', 'group')]),
        ),
    ]
