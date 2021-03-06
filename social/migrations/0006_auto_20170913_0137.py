# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20170913_0114'),
        ('social', '0005_auto_20170910_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberteam',
            old_name='person_id',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='memberteam',
            old_name='team_id',
            new_name='team',
        ),
        migrations.AddField(
            model_name='memberteam',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_team', to='person.Person', verbose_name='Лидер'),
        ),
    ]
