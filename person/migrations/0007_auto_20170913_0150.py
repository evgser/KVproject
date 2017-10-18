# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20170913_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Телефон'),
        ),
    ]
