# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20170913_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberteam',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_lead', to='person.Person', verbose_name='Лидер'),
        ),
    ]