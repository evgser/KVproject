# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20170912_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город'),
        ),
    ]
