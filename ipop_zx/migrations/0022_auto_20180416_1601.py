# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0021_auto_20180416_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedip',
            name='sql_createtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='usedip',
            name='utime',
            field=models.DateTimeField(default='2018-04-16 16:01:36'),
        ),
    ]
