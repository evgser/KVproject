# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20170914_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberteam',
            name='role',
            field=models.CharField(default=None, max_length=16, null=True, verbose_name='Роль'),
        ),
    ]
