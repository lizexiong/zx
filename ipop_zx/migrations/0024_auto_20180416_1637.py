# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0023_auto_20180416_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedip',
            name='sql_createtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usedip',
            name='utime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
