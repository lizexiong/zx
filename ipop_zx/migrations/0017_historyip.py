# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipop_zx', '0016_auto_20180413_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('username', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('password', models.CharField(blank=True, default='None', max_length=32, null=True)),
                ('mysql_username', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('mysql_password', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('mongo_username', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('mongo_password', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('other_username', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('other_password', models.CharField(blank=True, default='None', max_length=16, null=True)),
                ('group', models.CharField(max_length=32)),
                ('ip', models.GenericIPAddressField()),
                ('mask', models.CharField(default='255.255.255.0', max_length=32)),
                ('mac', models.CharField(blank=True, max_length=32, null=True)),
                ('os_type', models.CharField(blank=True, max_length=32, null=True)),
                ('hostname', models.CharField(blank=True, max_length=32, null=True)),
                ('createtime', models.CharField(max_length=32)),
                ('interface', models.CharField(blank=True, max_length=16, null=True)),
                ('network', models.CharField(blank=True, max_length=16, null=True)),
                ('open_port', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.CharField(blank=True, max_length=64, null=True)),
                ('url2', models.CharField(blank=True, max_length=64, null=True)),
                ('url3', models.CharField(blank=True, max_length=64, null=True)),
                ('url4', models.CharField(blank=True, max_length=64, null=True)),
                ('url5', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.CharField(blank=True, default='已删除', max_length=16, null=True)),
                ('content', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
